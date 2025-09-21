"""
Name: Merrick Moncure
Date: 9/21/2025
Assignment: Module 4 – Key/Value (pickleDB) Menu App
Due Date: 9/21/25
About this project:
    Part 1) SQLite DB Creation
- Drops the table if it already exists
- Creates a table with five attributes plus an auto-incrementing primary key
- Inserts at least six rows of data
- Uses a SELECT statement to display all rows
Assumptions:

All work below was performed by Merrick Moncure
"""
import sqlite3
from datetime import date

DB_PATH = "part1_items.db"

def main():
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()

        # ----- DDL: drop + create -----
        cur.execute("DROP TABLE IF EXISTS inventory_items;")
        cur.execute(
            """
            CREATE TABLE inventory_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                quantity INTEGER NOT NULL CHECK (quantity BETWEEN 1 AND 10000),
                price REAL NOT NULL CHECK (price > 0.0 AND price < 100000.0),
                entry_date TEXT NOT NULL
            );
            """
        )

        # ----- DML: insert ≥ 6 rows -----
        today = date.today().isoformat()
        rows = [
            ("Widget Pro", "Gadgets", 25, 99.99, today),
            ("Widget Mini", "Gadgets", 120, 39.5, today),
            ("Turbo Hammer", "Tools", 10, 59.0, "2025-07-04"),
            ("Precision Saw", "Tools", 5, 149.95, "2025-08-12"),
            ("Ultra Lamp", "HomeGoods", 50, 24.99, "2025-09-01"),
            ("Ergo Chair", "HomeGoods", 8, 219.0, today),
        ]
        cur.executemany(
            "INSERT INTO inventory_items (name, category, quantity, price, entry_date) "
            "VALUES (?, ?, ?, ?, ?);",
            rows,
        )
        conn.commit()

        # ----- SELECT + display all rows -----
        cur.execute(
            "SELECT id, name, category, quantity, price, entry_date "
            "FROM inventory_items ORDER BY id;"
        )
        results = cur.fetchall()

        print("\nAll rows in inventory_items:")
        print("-" * 80)
        header = f"{'ID':<4} {'Name':<20} {'Category':<12} {'Qty':>5} {'Price($)':>10} {'Date':>12}"
        print(header)
        print("-" * 80)
        for (id_, name, category, qty, price, d) in results:
            print(f"{id_:<4} {name:<20} {category:<12} {qty:>5} {price:>10.2f} {d:>12}")
        print("-" * 80)

    finally:
        conn.close()

if __name__ == "__main__":
    main()