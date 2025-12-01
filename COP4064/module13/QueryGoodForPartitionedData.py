"""
Name: Merrick Moncure
Date: 11/30/2025
Assignment: Column Store Project – Part 1 (QueryGoodForPartitionedData.py)
Due Date: 11/30/2025

About this script:
- Runs the same aggregation query on:
  * merge table fast_food_orders_merged (partitioned by items_count)
  * base table fast_food_orders
- Displays query results and execution time for both
- Query focuses on large orders (items_count >= 7) to benefit from partition pruning
"""

import time
import pymonetdb

MONETDB_HOST = "localhost"
MONETDB_PORT = 50000
MONETDB_USER = "monetdb"
MONETDB_PASSWORD = "monetdb"
MONETDB_DATABASE = "demo"

BASE_TABLE = "fast_food_orders"
MERGE_TABLE = "fast_food_orders_merged"


def get_connection():
    return pymonetdb.connect(
        username=MONETDB_USER,
        password=MONETDB_PASSWORD,
        hostname=MONETDB_HOST,
        port=MONETDB_PORT,
        database=MONETDB_DATABASE,
    )


QUERY = """
SELECT
    cuisine_type,
    COUNT(*)       AS num_orders,
    AVG(order_value) AS avg_order_value,
    AVG(delivery_time_minutes) AS avg_delivery_time
FROM {table_name}
WHERE items_count >= 7
GROUP BY cuisine_type
ORDER BY avg_order_value DESC;
"""


def run_query(table_name: str):
    conn = get_connection()
    cur = conn.cursor()
    try:
        sql = QUERY.format(table_name=table_name)
        start = time.perf_counter()
        cur.execute(sql)
        rows = cur.fetchall()
        elapsed = time.perf_counter() - start
    finally:
        cur.close()
        conn.close()
    return rows, elapsed


def print_results(label: str, rows, elapsed: float):
    print(f"\n=== Results for {label} ===")
    if not rows:
        print("No rows returned.\n")
        return
    print(f"{'Cuisine':<15} {'Num_Orders':>11} {'Avg_Value':>12} {'Avg_Delivery':>14}")
    print("-" * 60)
    for cuisine, num_orders, avg_val, avg_del in rows:
        print(
            f"{cuisine:<15} {int(num_orders):>11d} {float(avg_val):>12.2f} {float(avg_del):>14.2f}"
        )
    print(f"\nExecution time: {elapsed:.6f} seconds\n")


def main():
    merged_rows, merged_time = run_query(MERGE_TABLE)
    base_rows, base_time = run_query(BASE_TABLE)

    print_results("MERGE TABLE (partitioned)", merged_rows, merged_time)
    print_results("BASE TABLE (non-partitioned)", base_rows, base_time)


if __name__ == "__main__":
    main()
