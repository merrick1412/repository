"""
Name: Merrick Moncure
Date: 11/23/2025
Assignment: Module 4 – Column Store vs Relational DB
Due Date: 11/30/25
About this project:
- Create a relational database in SQLite from a raw Kaggle data file
  * Drops the table if it exists
  * Creates a table with all attributes in StudentsPerformance (1).csv
  * Loads the CSV data into the SQLite table

Assumptions:
- SQLite database file will be created in the current directory
- The CSV file 'StudentsPerformance (1).csv' is located in the same directory as this script
- All work below was performed by Merrick Moncure
"""

import csv
import sqlite3
from pathlib import Path

SQLITE_DB_FILENAME = "students_performance.sqlite"
CSV_FILENAME = "StudentsPerformance (1).csv"
TABLE_NAME = "students_performance"


def get_sqlite_connection():
    """Create and return a SQLite connection."""
    return sqlite3.connect(SQLITE_DB_FILENAME)


def drop_table_if_exists(cur):
    cur.execute(f"DROP TABLE IF EXISTS {TABLE_NAME};")


def create_table(cur):
    """
    Create a table that matches all attributes in the CSV.

    Columns based on StudentsPerformance (1).csv.
    """
    create_sql = f"""
    CREATE TABLE {TABLE_NAME} (
        "gender"                       TEXT,
        "race/ethnicity"              TEXT,
        "parental level of education" TEXT,
        "lunch"                       TEXT,
        "test preparation course"     TEXT,
        "math score"                  INTEGER,
        "reading score"               INTEGER,
        "writing score"               INTEGER
    );
    """
    cur.execute(create_sql)


def load_csv_into_table(cur):
    csv_path = Path(__file__).parent / CSV_FILENAME
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            rows.append(
                (
                    row["gender"],
                    row["race/ethnicity"],
                    row["parental level of education"],
                    row["lunch"],
                    row["test preparation course"],
                    int(row["math score"]),
                    int(row["reading score"]),
                    int(row["writing score"]),
                )
            )

    insert_sql = f"""
        INSERT INTO {TABLE_NAME} (
            "gender",
            "race/ethnicity",
            "parental level of education",
            "lunch",
            "test preparation course",
            "math score",
            "reading score",
            "writing score"
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """
    cur.executemany(insert_sql, rows)


def main():
    conn = get_sqlite_connection()
    try:
        cur = conn.cursor()
        drop_table_if_exists(cur)
        create_table(cur)
        load_csv_into_table(cur)
        conn.commit()
        print(f"Successfully created and loaded SQLite table '{TABLE_NAME}'.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
