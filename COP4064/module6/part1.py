from pymongo import MongoClient
from bson import json_util
from pprint import pprint
import json
from typing import Iterable, Any

from pymongo import MongoClient
from bson import json_util
from pprint import pprint
import json
from typing import Iterable, Any

DB_NAME = "salesdata"
COLL_NAME = "sales"
DATASET_PATH = "sales.json"

def get_client():
    # Default local connection string
    return MongoClient("mongodb://localhost:27017")

def read_extended_json(path: str) -> Iterable[Any]:
    """
    Supports two formats:
    1) NDJSON (one JSON document per line)
    2) A single JSON array of documents
    Uses bson.json_util to correctly parse MongoDB Extended JSON ($date, $oid, $numberDecimal, etc).
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().strip()
        if not text:
            return []

        # Try array first
        try:
            data = json_util.loads(text)
            if isinstance(data, list):
                return data
            # If it's a single object, wrap into a list
            return [data]
        except Exception:
            pass

    # Fall back to NDJSON mode (line by line)
    docs = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            docs.append(json_util.loads(line))
    return docs

def main():
    client = get_client()

    # Drop and recreate database/collection
    client.drop_database(DB_NAME)
    db = client[DB_NAME]
    coll = db[COLL_NAME]

    # Read the JSON dataset and insert
    docs = list(read_extended_json(DATASET_PATH))
    if not docs:
        print("No documents read from file. Check DATASET_PATH.")
        return

    coll.insert_many(docs)
    print(f"Inserted {coll.count_documents({})} documents into {DB_NAME}.{COLL_NAME}.")

    # Display ALL items (no limit)
    print("\nAll items (ALL shown):")
    for doc in coll.find({}):
        pprint(doc)

    print("\nDone.")

if __name__ == "__main__":
    main()