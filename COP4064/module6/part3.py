"""
Name: Merrick Moncure
Date: 10/05/2025
Assignment: Document DB Part 3 - Menu App (Sales)
Due Date: 10/05/2025

About this project:
- Menu-driven CLI for MongoDB collection cs_documentdb_demo.sales
- Options: Add item, Display All, Display Specific by unique receiptId, Quit
- Validates inputs per rubric (whole number range, real number range, non-empty strings with min length)
"""

# ### Part 3) Document DB Basic App (45 points)

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, ServerSelectionTimeoutError
from bson.decimal128 import Decimal128
from bson.objectid import ObjectId
from decimal import Decimal
from tabulate import tabulate

MONGO_URI = "mongodb://127.0.0.1:27017/?serverSelectionTimeoutMS=5000"
DB_NAME = "cs_documentdb_demo"
COLL_NAME = "sales"

# ---------------------- DB helpers ----------------------

def get_coll():
    """Connect, ping, and return the collection. Create a unique (sparse) index on receiptId."""
    client = MongoClient(MONGO_URI)
    try:
        client.admin.command("ping")
    except ServerSelectionTimeoutError:
        print("Cannot connect to MongoDB at 127.0.0.1:27017. Start mongod and try again.")
        raise
    db = client[DB_NAME]
    coll = db[COLL_NAME]
    # Enforce uniqueness for our app's ID while allowing existing docs without receiptId
    coll.create_index("receiptId", unique=True, sparse=True)
    return coll

# ---------------------- Input validation ----------------------

def prompt_nonempty_string(prompt: str, min_len: int = 3) -> str:
    while True:
        s = input(prompt).strip()
        if len(s) >= min_len:
            return s
        print(f"Input must be at least {min_len} characters and not blank.")

def prompt_int(prompt: str, min_val: int | None = None, max_val: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Enter a whole number in range [{min_val}, {max_val}]")
                continue
            return val
        except ValueError:
            print("Enter a valid whole number.")

def prompt_float(prompt: str, min_val: float | None = None, max_val: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Enter a real number in range [{min_val}, {max_val}]")
                continue
            return val
        except ValueError:
            print("Enter a valid real number.")

# ---------------------- Computation helpers for existing docs ----------------------

def dec(value) -> Decimal:
    """Convert Decimal128/float/int to Decimal safely."""
    if isinstance(value, Decimal128):
        return value.to_decimal()
    if isinstance(value, Decimal):
        return value
    if isinstance(value, (int, float)):
        return Decimal(str(value))
    return Decimal("0")

def compute_item_count(doc) -> int:
    """Sum items[].quantity if present; else fall back to stored itemCount or 0."""
    if isinstance(doc.get("items"), list):
        total = 0
        for it in doc["items"]:
            q = it.get("quantity", 0)
            try:
                total += int(q)
            except Exception:
                pass
        return total
    return int(doc.get("itemCount") or 0)

def compute_order_total(doc) -> float:
    """Sum items[].price * quantity if present; else fall back to stored orderTotal or 0.0."""
    if isinstance(doc.get("items"), list):
        total = Decimal("0")
        for it in doc["items"]:
            price = dec(it.get("price"))
            qty = it.get("quantity", 0)
            try:
                total += price * Decimal(int(qty))
            except Exception:
                pass
        return float(total)
    # fall back
    v = doc.get("orderTotal")
    if isinstance(v, Decimal128):
        return float(v.to_decimal())
    try:
        return float(v)
    except Exception:
        return 0.0

def get_customer_subs(doc):
    cust = doc.get("customer") or {}
    # Ensure we always have 3 subs; defaults if missing
    gender = cust.get("gender", "")
    age = cust.get("age", "")
    # Some seed docs use int for satisfaction; our inserted ones may use float; both are fine
    satisfaction = cust.get("satisfaction", "")
    return gender, age, satisfaction

# ---------------------- Menu actions ----------------------

def add_item(coll):
    print("\nAdd a new sale (enter values; validation enforced)")

    # Four non-dictionary attributes with validation:
    receipt_id = prompt_nonempty_string("Enter unique receiptId (min 3 chars): ", min_len=3)        # string min length
    store_location = prompt_nonempty_string("Enter storeLocation (min 3 chars): ", min_len=3)        # string min length
    purchase_method = prompt_nonempty_string("Enter purchaseMethod (min 3 chars): ", min_len=3)      # string min length
    item_count = prompt_int("Enter itemCount (0 to 10000): ", min_val=0, max_val=10000)              # whole number + range
    order_total = prompt_float("Enter orderTotal (0.00 to 100000.00): ", min_val=0.0, max_val=100000.0)  # real number + range

    # Dictionary attribute with 3 sub-attributes (includes whole and real numbers)
    customer_defaults = {
        "gender": "U",       # string
        "age": 30,           # whole number sub-attribute
        "satisfaction": 4.0  # real number sub-attribute
    }

    doc = {
        "receiptId": receipt_id,
        "storeLocation": store_location,
        "purchaseMethod": purchase_method,
        "itemCount": item_count,
        "orderTotal": order_total,
        "couponUsed": False,     # an extra top-level boolean (optional)
        "customer": customer_defaults
    }

    try:
        coll.insert_one(doc)
        print("Item added.")
    except DuplicateKeyError:
        print("That receiptId already exists. Item not added.")

def display_all(coll):
    print("\nAll items (showing 4 top-level attrs + 3 customer sub-attrs)")
    # Build rows for all documents, computing totals if not stored
    rows = []
    cursor = coll.find({}, {"_id": 1, "receiptId": 1, "storeLocation": 1, "purchaseMethod": 1,
                            "itemCount": 1, "orderTotal": 1, "items": 1, "customer": 1})
    for d in cursor:
        # Unique field for display: prefer receiptId, else show ObjectId
        unique_display = d.get("receiptId") or str(d.get("_id"))
        # Ensure itemCount and orderTotal exist (compute if missing)
        icount = d.get("itemCount")
        if icount is None:
            icount = compute_item_count(d)
        ototal = d.get("orderTotal")
        if ototal is None:
            ototal = compute_order_total(d)
        gender, age, satisfaction = get_customer_subs(d)
        rows.append([
            unique_display,
            d.get("storeLocation", ""),
            d.get("purchaseMethod", ""),
            icount,
            f"{ototal:.2f}" if isinstance(ototal, (int, float)) else ototal,
            gender, age, satisfaction
        ])
    headers = ["receiptId/_id", "storeLocation", "purchaseMethod", "itemCount", "orderTotal",
               "customer.gender", "customer.age", "customer.satisfaction"]
    if rows:
        print(tabulate(rows, headers=headers, tablefmt="github"))
    else:
        print("No documents found. Use 'Add' to insert one.")

def display_specific(coll):
    print("\nDisplay a specific item by receiptId")
    rid = input("Enter receiptId: ").strip()
    if not rid:
        print("receiptId cannot be blank.")
        return

    d = coll.find_one({"receiptId": rid}, {"_id": 1, "receiptId": 1, "storeLocation": 1, "purchaseMethod": 1,
                                           "itemCount": 1, "orderTotal": 1, "items": 1, "customer": 1})
    if not d:
        print("No item found with that receiptId.")
        return

    icount = d.get("itemCount")
    if icount is None:
        icount = compute_item_count(d)
    ototal = d.get("orderTotal")
    if ototal is None:
        ototal = compute_order_total(d)
    gender, age, satisfaction = get_customer_subs(d)

    rows = [[
        d.get("receiptId") or str(d.get("_id")),
        d.get("storeLocation", ""),
        d.get("purchaseMethod", ""),
        icount,
        f"{ototal:.2f}" if isinstance(ototal, (int, float)) else ototal,
        gender, age, satisfaction
    ]]
    headers = ["receiptId/_id", "storeLocation", "purchaseMethod", "itemCount", "orderTotal",
               "customer.gender", "customer.age", "customer.satisfaction"]
    print(tabulate(rows, headers=headers, tablefmt="github"))

# ---------------------- Menu loop ----------------------

def main():
    coll = get_coll()
    while True:
        print("\nMain Menu")
        print("A) Add an item")
        print("B) Display All items")
        print("C) Display a specific item")
        print("Q) Quit")
        choice = input("Select an option: ").strip().upper()
        if choice not in {"A", "B", "C", "Q"}:
            print("Invalid option. Please choose A, B, C, or Q.")
            continue
        if choice == "A":
            add_item(coll)
        elif choice == "B":
            display_all(coll)
        elif choice == "C":
            display_specific(coll)
        else:
            print("Goodbye.")
            break

if __name__ == "__main__":
    main()