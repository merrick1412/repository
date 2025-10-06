"""
Name: Merrick Moncure
Date: 10/05/2025
Assignment: Document DB Part 1 - Creation and Inserts
Due Date: 10/05/2025
About this project:
- Connects to local MongoDB
- Drops and recreates a database and collection
- Inserts 10+ items that satisfy attribute constraints
- Displays all items using find()
"""
from pymongo import MongoClient
from pprint import pprint

DB_NAME = "cs_documentdb_demo"
COLL_NAME = "devices"

def get_client():
    # Default local connection
    return MongoClient("mongodb://localhost:27017")

def main():
    # Connect to MongoDB
    client = get_client()

    # Drop the database if it exists
    client.drop_database(DB_NAME)

    # Create the database and collection by referencing them
    db = client[DB_NAME]
    coll = db[COLL_NAME]

    # Prepare at least 10 items
    # Requirements recap:
    # - At least 5 attributes per item
    # - One attribute unique per item (sku)
    # - At least 1 whole number attribute (quantity)
    # - At least 1 real number attribute (price)
    # - At least 1 dictionary with 3+ sub attributes (specs)
    #   with at least 1 whole number and 1 real number sub attribute
    base_items = [
        {
            "sku": f"SKU-{i:03d}",                  # unique string
            "name": name,
            "category": category,
            "quantity": 5 * i,                      # whole number
            "price": round(19.99 + i * 3.25, 2),    # real number
            "brand": brand,
            "specs": {
                "warranty_months": 12 + (i % 6),    # whole number sub attribute
                "weight_grams": 120.5 + i * 10.0,   # real number sub attribute
                "rating": round(3.5 + (i % 5) * 0.3, 1)  # real number sub attribute
            }
        }
        for i, (name, category, brand) in enumerate([
            ("Pocket Phone X", "phone", "Acme"),
            ("Ultrabook 13", "laptop", "Acme"),
            ("Noise Buds", "audio", "Globex"),
            ("Tablet Mini", "tablet", "Globex"),
            ("GameStation Pro", "console", "Initech"),
            ("Action Cam 4K", "camera", "Acme"),
            ("Smart Watch Z", "wearable", "Umbrella"),
            ("Studio Mic", "audio", "Globex"),
            ("Router AX6000", "network", "Initech"),
            ("E-Reader Glow", "tablet", "Acme").replace("-","-"),
            # You can add more if desired
        ], start=1)
    ]

    # Insert many items
    coll.insert_many(base_items)

    # Display all items
    print("\\nAll items in collection:")
    for doc in coll.find({}):
        pprint(doc)

    print("\\nDone.")

if __name__ == "__main__":
    main()