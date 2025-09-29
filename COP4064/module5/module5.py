"""
Name: Merrick Moncure
Date: 9/28/2025
Assignment: Module 5 – Key/Value (pickleDB) Menu App
Due Date: 9/28/25
About this project:
- Starts from Module 4 (Laptop object in pickleDB) and extends it:
  * Add/Edit/Display/Delete current-day Laptop in pickleDB
  * Register (add) current Laptop to a relational DB (SQLite) table
  * Display all Laptops from the relational DB
  * Quit

- pickleDB:
  * Stores exactly one Laptop per day
  * KEY = today's ISO date "YYYY-MM-DD" (to match Module 3 approach)

- SQLite:
  * Table 'laptops' with 5 attributes + id + entry_date
  * DDL is created automatically if missing
Assumptions:

All work below was performed by Merrick Moncure
"""

import sys
import sqlite3
from datetime import date, datetime, timedelta, timezone
from typing import Dict, Any, Optional, List
import pickledb

SQLITE_PATH = "laptops_part2.db"
KV_PATH = "laptops_kv.db"
TABLE = "laptops"

# =========================
# SQLite (Relational) Layer
# =========================

def ensure_schema():
    """Create laptops table if it doesn't exist."""
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {TABLE} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model_name TEXT NOT NULL,
                ram_gb INTEGER NOT NULL CHECK (ram_gb BETWEEN 2 AND 128),
                storage_gb INTEGER NOT NULL CHECK (storage_gb BETWEEN 64 AND 8192),
                screen_in REAL NOT NULL CHECK (screen_in >= 10.0 AND screen_in <= 18.4),
                price_usd REAL NOT NULL CHECK (price_usd > 0.0 AND price_usd <= 10000.0),
                entry_date TEXT NOT NULL
            );
            """
        )
        conn.commit()
    finally:
        conn.close()

def insert_laptop_row(item: Dict[str, Any]):
    """Insert a validated laptop dict into the relational table."""
    ensure_schema()
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            INSERT INTO {TABLE} (model_name, ram_gb, storage_gb, screen_in, price_usd, entry_date)
            VALUES (?, ?, ?, ?, ?, ?);
            """,
            (
                item["model_name"],
                int(item["ram_gb"]),
                int(item["storage_gb"]),
                float(item["screen_in"]),
                float(item["price_usd"]),
                item["entry_date"],
            ),
        )
        conn.commit()
    finally:
        conn.close()

def display_all_from_db():
    """Print all rows from the relational DB."""
    ensure_schema()
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        cur = conn.cursor()
        cur.execute(
            f"SELECT id, model_name, ram_gb, storage_gb, screen_in, price_usd, entry_date "
            f"FROM {TABLE} ORDER BY id;"
        )
        rows = cur.fetchall()
        if not rows:
            print("\nNo records in relational DB.\n")
            return
        print("\n-- All Laptops (relational DB) --")
        print(f"{'ID':<4} {'Model':<28} {'RAM':>5} {'Storage':>8} {'Screen':>8} {'Price($)':>12} {'Date':>12}")
        print("-" * 92)
        for (id_, model, ram, storage, screen, price, d) in rows:
            print(f"{id_:<4} {model:<28} {ram:>5} {storage:>8} {screen:>8.1f} {price:>12.2f} {d:>12}")
        print("-" * 92 + "\n")
    finally:
        conn.close()

# ======================
# pickleDB (KV) Helpers
# ======================

def load_kv():
    """Load pickleDB with auto_dump to persist on set/rem."""
    db = pickledb.PickleDB(KV_PATH)
    purge_expired(db)  # TTL on startup
    return db

# ---- TTL keys (delete > 3 days old) ----
TTL_DAYS = 3

def now_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def expires_in_days(days: int) -> str:
    return (datetime.now(timezone.utc) + timedelta(days=days)).isoformat(timespec="seconds")

def key_record(table: str, rec_id: int) -> str:
    return f"rec:{table}:{rec_id}"

def key_seq(table: str) -> str:
    return f"seq:{table}"

def key_today_map(d: str) -> str:
    return f"map:today:{d}"

def key_index(table: str, field: str, value: str) -> str:
    return f"idx:{table}:{field}:{value}"

def incr_counter(db, seq_key: str) -> int:
    """Get next sequence value (Enumerable Keys)."""
    if not db.get(seq_key):
        db.set(seq_key, 0)
    v = int(db.get(seq_key)) + 1
    db.set(seq_key, v)
    return v

def list_unique(lst: List[int]) -> List[int]:
    seen = set()
    out = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

def index_add(db, table: str, field: str, value: str, rec_id: int):
    key = key_index(table, field, value)
    arr = db.get(key) if db.get(key) else []
    if rec_id not in arr:
        arr.append(rec_id)
        db.set(key, list_unique(arr))

def index_remove(db, table: str, field: str, value: str, rec_id: int):
    key = key_index(table, field, value)
    if not db.get(key):
        return
    arr = [x for x in db.get(key) if x != rec_id]
    if arr:
        db.set(key, arr)
    else:
        db.rem(key)

def purge_expired(db):
    """Delete expired records and clean indexes."""
    # Scan all keys with prefix rec:laptops:
    for k in db.getall() if hasattr(db, "getall") else list(db.db.keys()):  # pickledb API variance
        if isinstance(k, bytes):
            k = k.decode("utf-8")
        if not str(k).startswith("rec:laptops:"):
            continue
        rec = db.get(k)
        if not isinstance(rec, dict):
            continue
        exp = rec.get("_meta", {}).get("expires_at")
        if not exp:
            continue
        try:
            if datetime.fromisoformat(exp) <= datetime.now(timezone.utc):
                # Remove from indexes first
                rid = rec.get("_id")
                if rid is not None:
                    if "model_name" in rec:
                        index_remove(db, "laptops", "model_name", str(rec["model_name"]), rid)
                    if "entry_date" in rec:
                        index_remove(db, "laptops", "entry_date", str(rec["entry_date"]), rid)
                db.rem(k)
        except Exception:
            # If timestamp malformed, delete defensively
            db.rem(k)

# ---- Emulating tables + Atomic aggregates ----

def table_get(db, table: str, rec_id: int) -> Optional[Dict[str, Any]]:
    k = key_record(table, rec_id)
    return db.get(k) if db.get(k) else None

def table_upsert_atomic(db, table: str, rec: Dict[str, Any]) -> int:
    """
    Atomic aggregate write:
    - Validate and build full record dict first.
    - Then perform a single db.set on rec key, and index updates.
    Returns record id.
    """
    # Assign ID if new
    if rec.get("_id") is None:
        rec["_id"] = incr_counter(db, key_seq(table))

    rid = int(rec["_id"])
    k = key_record(table, rid)

    # REQUIRED domain fields
    required = ["model_name", "ram_gb", "storage_gb", "screen_in", "price_usd", "entry_date", "subtype"]
    for r in required:
        if r not in rec:
            raise ValueError(f"Missing required field: {r}")

    # subtype-specific validation (Aggregates)
    st = rec["subtype"]
    if st == "gaming":
        if not rec.get("gpu_model"):
            raise ValueError("gaming subtype requires gpu_model")
    elif st == "ultrabook":
        if rec.get("battery_hrs") is None:
            raise ValueError("ultrabook subtype requires battery_hrs")
    elif st == "standard":
        pass
    else:
        raise ValueError("subtype must be standard|gaming|ultrabook")

    # Add/refresh TTL metadata
    meta = rec.get("_meta", {})
    if not meta.get("created_at"):
        meta["created_at"] = now_utc_iso()
    meta["expires_at"] = expires_in_days(TTL_DAYS)
    rec["_meta"] = meta

    # Previous record (for index diff)
    prev = db.get(k) if db.get(k) else None

    # SET ONCE atomically
    db.set(k, rec)

    # Maintain “today map” for UI
    today_map_key = key_today_map(rec["entry_date"])
    db.set(today_map_key, rid)

    # Maintain secondary indexes
    if prev:
        if prev.get("model_name"):
            index_remove(db, table, "model_name", str(prev["model_name"]), rid)
        if prev.get("entry_date"):
            index_remove(db, table, "entry_date", str(prev["entry_date"]), rid)
    index_add(db, table, "model_name", str(rec["model_name"]), rid)
    index_add(db, table, "entry_date", str(rec["entry_date"]), rid)

    return rid

def table_delete(db, table: str, rec_id: int):
    k = key_record(table, rec_id)
    if not db.get(k):
        return
    rec = db.get(k)
    if rec and isinstance(rec, dict):
        if rec.get("model_name"):
            index_remove(db, table, "model_name", str(rec["model_name"]), rec["_id"])
        if rec.get("entry_date"):
            index_remove(db, table, "entry_date", str(rec["entry_date"]), rec["_id"])
    db.rem(k)

# ---- “Today” convenience used by menu ----

def today_key() -> str:
    return date.today().isoformat()

def kv_has_today_item(db) -> bool:
    mkey = key_today_map(today_key())
    return db.get(mkey)

def kv_get_today_item(db) -> Dict[str, Any]:
    rid = db.get(key_today_map(today_key()))
    rec = table_get(db, "laptops", int(rid))
    return rec

def kv_set_today_item(db, item: Dict[str, Any]):
    # Either create new or update existing “today” record atomically
    mkey = key_today_map(today_key())
    if db.get(mkey):
        rid = int(db.get(mkey))
        item["_id"] = rid
    item["entry_date"] = today_key()
    table_upsert_atomic(db, "laptops", item)

def kv_delete_today_item(db):
    mkey = key_today_map(today_key())
    if not db.get(mkey):
        return
    rid = int(db.get(mkey))
    table_delete(db, "laptops", rid)
    db.rem(mkey)

# ====================
# Validation Routines
# ====================

def prompt_str(label: str, min_len: int = 3) -> str:
    while True:
        s = input(f"{label} (min {min_len} chars): ").strip()
        if len(s) >= min_len:
            return s
        print(f"Invalid. {label} must be at least {min_len} characters.")

def prompt_int(label: str, lo: int, hi: int) -> int:
    while True:
        raw = input(f"{label} (integer {lo}-{hi}): ").strip()
        try:
            v = int(raw)
            if lo <= v <= hi:
                return v
            print(f"{label} must be between {lo} and {hi}.")
        except ValueError:
            print(f"{label} must be an integer.")

def prompt_float(label: str, lo: float, hi: float, inclusive_low: bool = True, inclusive_high: bool = True) -> float:
    low_op = ">=" if inclusive_low else ">"
    high_op = "<=" if inclusive_high else "<"
    while True:
        raw = input(f"{label} (number {low_op} {lo} and {high_op} {hi}): ").strip()
        try:
            v = float(raw)
            ok_low = (v >= lo) if inclusive_low else (v > lo)
            ok_high = (v <= hi) if inclusive_high else (v < hi)
            if ok_low and ok_high:
                return v
            print(f"{label} must be {low_op} {lo} and {high_op} {hi}.")
        except ValueError:
            print(f"{label} must be a real number.")

def prompt_subtype() -> str:
    while True:
        s = input("Subtype [standard|gaming|ultrabook]: ").strip().lower()
        if s in {"standard","gaming","ultrabook"}:
            return s
        print("Enter one of: standard, gaming, ultrabook")

# ====================
# Laptop CRUD Flows
# ====================

def add_flow(db):
    """Add a new Laptop for today (only when one does NOT already exist)."""
    if kv_has_today_item(db):
        print("A Laptop for today already exists. Use Edit instead.\n")
        return

    # Common attributes
    item = {
        "model_name": prompt_str("Model name", 3),
        "ram_gb": prompt_int("RAM (GB)", 2, 128),
        "storage_gb": prompt_int("Storage (GB)", 64, 8192),
        "screen_in": prompt_float("Screen size (inches)", 10.0, 18.4),
        "price_usd": prompt_float("Price (USD)", 0.01, 10000.0, inclusive_low=False, inclusive_high=True),
        "subtype": prompt_subtype(),
    }

    # Aggregates: subtype-specific fields
    if item["subtype"] == "gaming":
        item["gpu_model"] = prompt_str("GPU model", 3)
    elif item["subtype"] == "ultrabook":
        item["battery_hrs"] = prompt_float("Battery life (hours)", 1.0, 36.0)

    kv_set_today_item(db, item)
    print("\nSaved today's Laptop to pickleDB.\n")

def edit_flow(db):
    """Edit the existing Laptop for today (only when one exists)."""
    if not kv_has_today_item(db):
        print("No Laptop for today to edit. Use Add first.\n")
        return
    current = kv_get_today_item(db)
    print("\n-- Current Laptop (today) --")
    for k, v in current.items():
        if k == "_meta":
            continue
        print(f"{k}: {v}")
    print("----------------------------")

    def edit_str(label, current_val, min_len=3):
        s = input(f"{label} [{current_val}]: ").strip()
        return current_val if s == "" else (s if len(s) >= min_len else current_val)

    def edit_int(label, current_val, lo, hi):
        s = input(f"{label} [{current_val}]: ").strip()
        if s == "":
            return current_val
        try:
            v = int(s);  assert lo <= v <= hi
            return v
        except Exception:
            print("Invalid; keeping previous value.")
            return current_val

    def edit_float(label, current_val, lo, hi, inclusive_low=True, inclusive_high=True):
        s = input(f"{label} [{current_val}]: ").strip()
        if s == "":
            return current_val
        try:
            v = float(s)
            ok_low = (v >= lo) if inclusive_low else (v > lo)
            ok_high = (v <= hi) if inclusive_high else (v < hi)
            if ok_low and ok_high:
                return v
        except Exception:
            pass
        print("Invalid; keeping previous value.")
        return current_val

    updated = dict(current)  # start from current
    updated["model_name"] = edit_str("Model name", current["model_name"], 3)
    updated["ram_gb"] = edit_int("RAM (GB)", current["ram_gb"], 2, 128)
    updated["storage_gb"] = edit_int("Storage (GB)", current["storage_gb"], 64, 8192)
    updated["screen_in"] = edit_float("Screen size (inches)", current["screen_in"], 10.0, 18.4)
    updated["price_usd"] = edit_float("Price (USD)", current["price_usd"], 0.01, 10000.0, inclusive_low=False, inclusive_high=True)

    # subtype cannot change here to keep indexes simple
    if current["subtype"] == "gaming":
        updated["gpu_model"] = edit_str("GPU model", current.get("gpu_model",""), 3)
    elif current["subtype"] == "ultrabook":
        updated["battery_hrs"] = edit_float("Battery life (hours)", float(current.get("battery_hrs", 1.0)), 1.0, 36.0)

    kv_set_today_item(db, updated)
    print("\nUpdated today's Laptop in pickleDB.\n")

def display_flow(db):
    """Display current Laptop (today) if present."""
    if not kv_has_today_item(db):
        print("No Laptop for today to display.\n")
        return
    item = kv_get_today_item(db)
    print("\n-- Today's Laptop (pickleDB) --")
    for k in ["_id","model_name","ram_gb","storage_gb","screen_in","price_usd","entry_date","subtype","gpu_model","battery_hrs"]:
        if k in item:
            val = item[k]
            if k == "screen_in":
                val = f"{float(val):.1f}"
            elif k == "price_usd":
                val = f"{float(val):,.2f}"
            print(f"{k:>12}: {val}")
    print()

def delete_flow(db):
    """Delete the current-day Laptop from pickleDB."""
    if not kv_has_today_item(db):
        print("Nothing to delete; no Laptop for today.\n")
        return
    kv_delete_today_item(db)
    print("\nDeleted today's Laptop from pickleDB.\n")

def register_flow(db):
    """Add current-day Laptop to relational DB; then clear pickleDB."""
    if not kv_has_today_item(db):
        print("No Laptop for today to register.\n")
        return
    item = kv_get_today_item(db)
    insert_laptop_row(item)
    kv_delete_today_item(db)
    print("\nRegistered Laptop to relational DB and cleared pickleDB.\n")

# ------ small demo search via index (shows Indexes working) ------

def search_by_model_prefix(db):
    prefix = input("Model prefix: ").strip()
    if not prefix:
        return
    # enumerate index buckets that match the prefix
    print("\nMatches:")
    count = 0
    for key in db.getall() if hasattr(db, "getall") else list(db.db.keys()):
        if isinstance(key, bytes):
            key = key.decode("utf-8")
        if key.startswith("idx:laptops:model_name:") and str(key).split("idx:laptops:model_name:",1)[1].startswith(prefix):
            ids = db.get(key)
            for rid in ids:
                rec = table_get(db, "laptops", int(rid))
                if rec:
                    print(f"- [{rid}] {rec['model_name']} ({rec['entry_date']})")
                    count += 1
    if count == 0:
        print("  No matches.\n")
    else:
        print()

# ==============
# Menu & Driver
# ==============

def print_menu(has_today: bool):
    print("\n====== Main Menu ======")
    if not has_today:
        print("A) Add Laptop (pickleDB)")
        print("H) Display ALL Laptops from relational DB")
        print("S) Search laptops by model prefix (KV index demo)")
        print("Q) Quit")
    else:
        print("A) Edit Laptop (pickleDB)")
        print("B) Display Laptop (pickleDB)")
        print("D) Delete Laptop (pickleDB)")
        print("G) Register Laptop to relational DB")
        print("H) Display ALL Laptops from relational DB")
        print("S) Search laptops by model prefix (KV index demo)")
        print("Q) Quit")
    print("=======================\n")

def get_valid_choice(has_today: bool) -> str:
    valid = {"H", "Q", "S"}
    if not has_today:
        valid.add("A")
    else:
        valid.update({"A", "B", "D", "G"})
    while True:
        choice = input("Enter choice: ").strip().upper()
        if choice in valid:
            return choice
        print(f"Invalid choice. Valid options: {', '.join(sorted(valid))}")

def main():
    ensure_schema()
    db = load_kv()

    while True:
        purge_expired(db)  # TTL sweep each loop
        has_today = kv_has_today_item(db)
        print_menu(has_today)
        choice = get_valid_choice(has_today)

        if choice == "Q":
            print("Goodbye!")
            break
        elif choice == "H":
            display_all_from_db()
        elif choice == "S":
            search_by_model_prefix(db)
        elif choice == "A" and not has_today:
            add_flow(db)
        elif choice == "A" and has_today:
            edit_flow(db)
        elif choice == "B":
            display_flow(db)
        elif choice == "D":
            delete_flow(db)
        elif choice == "G":
            register_flow(db)
        else:
            print("Unhandled option. Please try again.\n")

if __name__ == "__main__":
    main()