"""
Name: Merrick Moncure
Date: 10/05/2025
Assignment: Document DB Part 2 - Querying
Due Date: 10/05/2025
About this project:
- Connects to the Part 1 MongoDB database/collection
- Runs the six required finds with projections, filters, and sorts
- Displays results in table format using tabulate
"""
from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import ServerSelectionTimeoutError
from bson import json_util, Decimal128
from datetime import datetime
from tabulate import tabulate

MONGO_URI = "mongodb://127.0.0.1:27017/?serverSelectionTimeoutMS=5000"
DB_NAME = "cs_documentdb_demo"
COLL_NAME = "sales"

def printable(value):
    """Make any BSON/complex value readable for tables."""
    if isinstance(value, Decimal128):
        return float(value.to_decimal())
    if isinstance(value, datetime):
        return value.isoformat()
    # For dicts/arrays/ObjectId/etc use Extended JSON
    return json_util.dumps(value, ensure_ascii=False)

def as_table_rows(docs, headers=None):
    """Convert a list of documents to tabular rows (stringifying nested fields)."""
    if not docs:
        return [], []
    if headers is None:
        # Union of top-level keys across docs
        keys = set()
        for d in docs:
            keys.update(d.keys())
        headers = sorted(keys)
    rows = []
    for d in docs:
        rows.append([printable(d.get(k, "")) for k in headers])
    return headers, rows

def print_header(title):
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title))

def main():
    # Connect and ping so we fail fast if mongod isn't up
    try:
        client = MongoClient(MONGO_URI)
        client.admin.command("ping")
    except ServerSelectionTimeoutError:
        print("Cannot connect to MongoDB at 127.0.0.1:27017. Start mongod and try again.")
        return

    db = client[DB_NAME]
    coll = db[COLL_NAME]

    # 1) One item: show key name, data type, and sample value
    print_header("1) One item — keys, data types, sample values")
    one = coll.find_one({})
    if not one:
        print("No documents found in collection. Run Part 1 first.")
        return
    rows = []
    for k, v in one.items():
        rows.append([k, type(v).__name__, (printable(v) if len(printable(v)) <= 120 else printable(v)[:117] + "...")])
    print(tabulate(rows, headers=["Key", "Type", "Sample Value"], tablefmt="github"))

    # Common projection for steps 2 & 3 (four attributes)
    projection4 = {"_id": 0, "storeLocation": 1, "purchaseMethod": 1, "couponUsed": 1, "saleDate": 1}

    # 2) Find with projection to four attributes; table output
    print_header("2) Projection to four attributes (table)")
    docs_2 = list(coll.find({}, projection4).limit(25))
    print(tabulate(docs_2, headers="keys", tablefmt="github"))

    # 3) Same find, sorted by two attributes: storeLocation ASC, saleDate DESC
    print_header("3) Sorted by storeLocation ASC, saleDate DESC (table)")
    docs_3 = list(coll.find({}, projection4).sort([
        ("storeLocation", ASCENDING),
        ("saleDate", DESCENDING)
    ]).limit(25))
    print(tabulate(docs_3, headers="keys", tablefmt="github"))

    # 4) Find: display ALL attributes but limit items to match sets on two attributes; table output
    # Use common values from the sample dataset; if zero, fall back to dynamic distincts.
    print_header("4) All attributes where storeLocation in {Seattle, Denver} "
                 "AND purchaseMethod in {In store, Online} (table)")
    base_filter = {
        "storeLocation": {"$in": ["Seattle", "Denver"]},
        "purchaseMethod": {"$in": ["In store", "Online"]}
    }
    docs_4 = list(coll.find(base_filter).limit(10))
    fallback_note = ""
    if not docs_4:
        # Fallback: derive sets from DB so we always return >= 1 item
        stores = coll.distinct("storeLocation")
        methods = coll.distinct("purchaseMethod")
        base_filter = {
            "storeLocation": {"$in": stores[:2] or stores},
            "purchaseMethod": {"$in": methods[:2] or methods}
        }
        docs_4 = list(coll.find(base_filter).limit(10))
        fallback_note = " (fallback to dynamic distincts)"
    headers_4, rows_4 = as_table_rows(docs_4)
    print(f"Filter used: {base_filter}{fallback_note}")
    print(tabulate(rows_4, headers=headers_4, tablefmt="github"))

    # 5) Same filter, but show ONLY three attributes; table output
    print_header("5) Same filter, only three attributes (table)")
    projection3 = {"_id": 0, "storeLocation": 1, "purchaseMethod": 1, "couponUsed": 1}
    docs_5 = list(coll.find(base_filter, projection3).limit(25))
    print(tabulate(docs_5, headers="keys", tablefmt="github"))

    # 6) Same filter & three-attribute projection; sort by one displayed attribute
    print_header("6) Sorted by purchaseMethod ASC (table)")
    docs_6 = list(coll.find(base_filter, projection3).sort([
        ("purchaseMethod", ASCENDING)
    ]).limit(25))
    print(tabulate(docs_6, headers="keys", tablefmt="github"))

    print("\nDone.")

if __name__ == "__main__":
    main()