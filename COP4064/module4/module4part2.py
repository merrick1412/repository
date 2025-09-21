"""
Name: Merrick Moncure
Date: 9/21/2025
Assignment: Module 4 – Key/Value (pickleDB) Menu App
Due Date: 9/21/25
About this project:
- Starts from Module 3 (Laptop object in pickleDB) and extends it:
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
from datetime import date
from typing import Dict, Any
from pickledb import PickleDB

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
    return PickleDB._load(KV_PATH, auto_dump=True)

def today_key() -> str:
    return date.today().isoformat()  # e.g., '2025-09-21'

def kv_has_today_item(db) -> bool:
    """Return True if today's key exists and value is a dict."""
    key = today_key()
    return db.exists(key) and isinstance(db.get(key), dict)

def kv_get_today_item(db) -> Dict[str, Any]:
    return db.get(today_key())

def kv_set_today_item(db, item: Dict[str, Any]):
    db.set(today_key(), item)

def kv_delete_today_item(db):
    key = today_key()
    if db.exists(key):
        db.rem(key)

# ====================
# Validation Routines
# ====================

def prompt_str(label: str, min_len: int = 5) -> str:
    while True:
        s = input(f"{label} (min {min_len} chars): ").strip()
        if len(s) >= min_len:
            return s
        print(f"Invalid. {label} must be at least {min_len} characters and not empty/whitespace.")

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

def prompt_today_date(label: str) -> str:
    """Force the entry date to match today, per assignment spec."""
    today = today_key()
    while True:
        s = input(f"{label} (YYYY-MM-DD) must equal {today}: ").strip()
        if s == today:
            return s
        print(f"{label} must exactly match today's date: {today}")

# ====================
# Laptop CRUD Flows
# ====================

def add_flow(db):
    """Add a new Laptop for today (only when one does NOT already exist)."""
    if kv_has_today_item(db):
        print("A Laptop for today already exists. Use Edit instead.\n")
        return
    item = {
        "model_name": prompt_str("Model name", 5),
        "ram_gb": prompt_int("RAM (GB)", 2, 128),
        "storage_gb": prompt_int("Storage (GB)", 64, 8192),
        "screen_in": prompt_float("Screen size (inches)", 10.0, 18.4),
        "price_usd": prompt_float("Price (USD)", 0.01, 10000.0, inclusive_low=False, inclusive_high=True),
        "entry_date": prompt_today_date("Entry date"),
    }
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
        print(f"{k}: {v}")
    print("----------------------------")

    def edit_str(label, current_val, min_len=5):
        while True:
            s = input(f"{label} [{current_val}]: ").strip()
            if s == "":
                return current_val
            if len(s) >= min_len:
                return s
            print(f"{label} must be at least {min_len} characters.")

    def edit_int(label, current_val, lo, hi):
        while True:
            s = input(f"{label} [{current_val}]: ").strip()
            if s == "":
                return current_val
            try:
                v = int(s)
                if lo <= v <= hi:
                    return v
                print(f"{label} must be between {lo} and {hi}.")
            except ValueError:
                print(f"{label} must be an integer.")

    def edit_float(label, current_val, lo, hi, inclusive_low=True, inclusive_high=True):
        low_op = ">=" if inclusive_low else ">"
        high_op = "<=" if inclusive_high else "<"
        while True:
            s = input(f"{label} [{current_val}] ({low_op} {lo}, {high_op} {hi}): ").strip()
            if s == "":
                return current_val
            try:
                v = float(s)
                ok_low = (v >= lo) if inclusive_low else (v > lo)
                ok_high = (v <= hi) if inclusive_high else (v < hi)
                if ok_low and ok_high:
                    return v
                print(f"{label} must be {low_op} {lo} and {high_op} {hi}.")
            except ValueError:
                print(f"{label} must be a real number.")

    def edit_today(label, current_val):
        t = today_key()
        while True:
            s = input(f"{label} [{current_val}] (must be {t}): ").strip()
            if s == "":
                s = current_val
            if s == t:
                return s
            print(f"{label} must equal today's date: {t}")

    updated = {
        "model_name": edit_str("Model name", current["model_name"], 5),
        "ram_gb": edit_int("RAM (GB)", current["ram_gb"], 2, 128),
        "storage_gb": edit_int("Storage (GB)", current["storage_gb"], 64, 8192),
        "screen_in": edit_float("Screen size (inches)", current["screen_in"], 10.0, 18.4),
        "price_usd": edit_float("Price (USD)", current["price_usd"], 0.01, 10000.0, inclusive_low=False, inclusive_high=True),
        "entry_date": edit_today("Entry date", current["entry_date"]),
    }
    kv_set_today_item(db, updated)
    print("\nUpdated today's Laptop in pickleDB.\n")

def display_flow(db):
    """Display current Laptop (today) if present."""
    if not kv_has_today_item(db):
        print("No Laptop for today to display.\n")
        return
    item = kv_get_today_item(db)
    print("\n-- Today's Laptop (pickleDB) --")
    print(f"{'Model':>12}: {item['model_name']}")
    print(f"{'RAM (GB)':>12}: {item['ram_gb']}")
    print(f"{'Storage':>12}: {item['storage_gb']}")
    print(f"{'Screen (in)':>12}: {float(item['screen_in']):.1f}")
    print(f"{'Price ($)':>12}: {float(item['price_usd']):,.2f}")
    print(f"{'Date':>12}: {item['entry_date']}\n")

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

# ==============
# Menu & Driver
# ==============

def print_menu(has_today: bool):
    print("\n====== Main Menu ======")
    if not has_today:
        print("A) Add Laptop (pickleDB)")
        print("H) Display ALL Laptops from relational DB")
        print("Q) Quit")
    else:
        print("A) Edit Laptop (pickleDB)")
        print("B) Display Laptop (pickleDB)")
        print("D) Delete Laptop (pickleDB)")
        print("G) Register Laptop to relational DB")
        print("H) Display ALL Laptops from relational DB")
        print("Q) Quit")
    print("=======================\n")

def get_valid_choice(has_today: bool) -> str:
    valid = {"H", "Q"}
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
        has_today = kv_has_today_item(db)
        print_menu(has_today)
        choice = get_valid_choice(has_today)

        if choice == "Q":
            print("Goodbye!")
            break
        elif choice == "H":
            display_all_from_db()
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