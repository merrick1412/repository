"""
Name: Merrick Moncure
Date: 11/30/2025
Assignment: Column Store Project – Part 2 (CreateSumaryTableDB.py)
Due Date: 11/30/2025

About this script:
- Builds a summary table from fast_food_orders2
- Stores at least two aggregated columns and at least two other columns
- Denormalizes per (city, cuisine_type) for efficient analytic queries
"""

import pymonetdb

MONETDB_HOST = "localhost"
MONETDB_PORT = 50000
MONETDB_USER = "monetdb"
MONETDB_PASSWORD = "monetdb"
MONETDB_DATABASE = "demo"

BASE_TABLE2 = "fast_food_orders2"
SUMMARY_TABLE = "fast_food_orders_summary"


def get_connection():
    return pymonetdb.connect(
        username=MONETDB_USER,
        password=MONETDB_PASSWORD,
        hostname=MONETDB_HOST,
        port=MONETDB_PORT,
        database=MONETDB_DATABASE,
    )


def drop_and_create_summary():
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(f"DROP TABLE IF EXISTS {SUMMARY_TABLE};")
        # Summary table with aggregated and non-aggregated columns
        cur.execute(
            f"""
            CREATE TABLE {SUMMARY_TABLE} AS
            SELECT
                city,
                cuisine_type,
                COUNT(*)                AS num_orders,
                AVG(order_value)        AS avg_order_value,
                AVG(delivery_time_minutes) AS avg_delivery_time,
                SUM(items_count)        AS total_items
            FROM {BASE_TABLE2}
            GROUP BY city, cuisine_type
            WITH DATA;
            """
        )
        conn.commit()
    finally:
        cur.close()
        conn.close()


def main():
    drop_and_create_summary()
    print(f"Created summary table '{SUMMARY_TABLE}' from '{BASE_TABLE2}'.")


if __name__ == "__main__":
    main()
