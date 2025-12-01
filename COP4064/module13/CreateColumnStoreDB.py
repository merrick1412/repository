"""
Name: Merrick Moncure
Date: 11/30/2025
Assignment: Column Store Project – Part 1 (CreateColumnStoreDB.py)
Due Date: 11/30/2025

About this script:
- Connects to a MonetDB column-store database using pymonetdb
- Drops and recreates a base table for the fast-food ordering dataset
- Loads all rows from fast_food_ordering_dataset.csv into the base table
"""

import csv
import pymonetdb


MONETDB_HOST = "localhost"
MONETDB_PORT = 50000
MONETDB_USER = "monetdb"
MONETDB_PASSWORD = "monetdb"
MONETDB_DATABASE = "demo"

CSV_PATH = "fast_food_ordering_dataset.csv"
BASE_TABLE = "fast_food_orders"


def get_connection():
    """Create and return a MonetDB connection."""
    return pymonetdb.connect(
        username=MONETDB_USER,
        password=MONETDB_PASSWORD,
        hostname=MONETDB_HOST,
        port=MONETDB_PORT,
        database=MONETDB_DATABASE,
    )


def drop_and_create_base_table():
    """Drop the base table if it exists and recreate it with all attributes."""
    ddl = f"""
    CREATE TABLE {BASE_TABLE} (
        order_id               VARCHAR(32) PRIMARY KEY,
        order_time             TIMESTAMP,
        city                   VARCHAR(64),
        cuisine_type           VARCHAR(64),
        order_value            DECIMAL(10,2),
        delivery_time_minutes  INT,
        payment_method         VARCHAR(64),
        items_count            INT
    );
    """

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(f"DROP TABLE IF EXISTS {BASE_TABLE};")
        cur.execute(ddl)
        conn.commit()
    finally:
        cur.close()
        conn.close()


def load_data_from_csv():
    """Load all rows from CSV into the base MonetDB table."""
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(
                {
                    "order_id": r["order_id"],
                    "order_time": r["order_time"],
                    "city": r["city"],
                    "cuisine_type": r["cuisine_type"],
                    "order_value": float(r["order_value"]),
                    "delivery_time_minutes": int(r["delivery_time_minutes"]),
                    "payment_method": r["payment_method"],
                    "items_count": int(r["items_count"]),
                }
            )

    conn = get_connection()
    cur = conn.cursor()
    try:
        sql = f"""
        INSERT INTO {BASE_TABLE} (
            order_id,
            order_time,
            city,
            cuisine_type,
            order_value,
            delivery_time_minutes,
            payment_method,
            items_count
        ) VALUES (
            %(order_id)s,
            %(order_time)s,
            %(city)s,
            %(cuisine_type)s,
            %(order_value)s,
            %(delivery_time_minutes)s,
            %(payment_method)s,
            %(items_count)s
        );
        """
        cur.executemany(sql, rows)
        conn.commit()
    finally:
        cur.close()
        conn.close()


def main():
    drop_and_create_base_table()
    load_data_from_csv()
    print(f"Loaded data into base table '{BASE_TABLE}'.")


if __name__ == "__main__":
    main()
