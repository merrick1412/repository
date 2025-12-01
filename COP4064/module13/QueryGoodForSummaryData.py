"""
Name: Merrick Moncure
Date: 11/30/2025
Assignment: Column Store Project – Part 2 (QueryGoodForSummaryData.py)
Due Date: 11/30/2025

About this script:
- Compares a query on the summary table vs the raw base table
- Same logical query: find (city, cuisine_type) pairs with high average order_value
- Displays results and execution time for both tables
"""

import time
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


# Threshold chosen so that at least one row is returned; adjust if needed.
AVG_THRESHOLD = 800.0


def run_on_summary():
    conn = get_connection()
    cur = conn.cursor()
    try:
        sql = f"""
        SELECT
            city,
            cuisine_type,
            num_orders,
            avg_order_value
        FROM {SUMMARY_TABLE}
        WHERE avg_order_value > {AVG_THRESHOLD}
        ORDER BY avg_order_value DESC;
        """
        start = time.perf_counter()
        cur.execute(sql)
        rows = cur.fetchall()
        elapsed = time.perf_counter() - start
    finally:
        cur.close()
        conn.close()
    return rows, elapsed


def run_on_base():
    conn = get_connection()
    cur = conn.cursor()
    try:
        sql = f"""
        SELECT
            city,
            cuisine_type,
            COUNT(*)         AS num_orders,
            AVG(order_value) AS avg_order_value
        FROM {BASE_TABLE2}
        GROUP BY city, cuisine_type
        HAVING AVG(order_value) > {AVG_THRESHOLD}
        ORDER BY avg_order_value DESC;
        """
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
    print(f"{'City':<15} {'Cuisine':<15} {'Num_Orders':>11} {'Avg_Value':>12}")
    print("-" * 60)
    for city, cuisine, num_orders, avg_val in rows:
        print(f"{city:<15} {cuisine:<15} {int(num_orders):>11d} {float(avg_val):>12.2f}")
    print(f"\nExecution time: {elapsed:.6f} seconds\n")


def main():
    summary_rows, summary_time = run_on_summary()
    base_rows, base_time = run_on_base()

    print_results("SUMMARY TABLE (denormalized)", summary_rows, summary_time)
    print_results("BASE TABLE (raw fact table)", base_rows, base_time)


if __name__ == "__main__":
    main()
