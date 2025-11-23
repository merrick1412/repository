"""
Name: Merrick Moncure
Date: 11/23/2025
Assignment: Module 4 – Column Store vs Relational DB
Due Date: 11/30/25
About this project:
- Create a column store database in MonetDB from a raw Kaggle data file
  * Drops the table if it exists
  * Creates a table with all attributes in StudentsPerformance (1).csv
  * Loads the CSV data into the MonetDB table

Assumptions:
- MonetDB server is running locally and reachable with the credentials below
- The CSV file 'StudentsPerformance (1).csv' is located in the same directory as this script
- All work below was performed by Merrick Moncure
"""

import csv
import os
from pathlib import Path

import pymonetdb  # pip install pymonetdb

# MonetDB connection settings
MONETDB_HOST = "localhost"
MONETDB_PORT = 50000
MONETDB_USER = "monetdb"
MONETDB_PASSWORD = "monetdb"
MONETDB_DBNAME = "demo"

CSV_FILENAME = "StudentsPerformance (1).csv"
TABLE_NAME = "students_performance"


def get_monetdb_connection():
    """Create and return a MonetDB connection."""
    conn = pymonetdb.connect(
        hostname=MONETDB_HOST,
        port=MONETDB_PORT,
        username=MONETDB_USER,
        password=MONETDB_PASSWORD,
        database=MONETDB_DBNAME,
    )
    return conn


def drop_table_if_exists(cur):
    """Drop the students_performance table if it exists."""
    cur.execute(f"DROP TABLE IF EXISTS {TABLE_NAME};")


def create_table(cur):
    """
    Create a table that matches all attributes in the CSV.

    Columns based on StudentsPerformance (1).csv:
    - gender (string)
    - race/ethnicity (string)
    - parental level of education (string)
    - lunch (string)
    - test preparation course (string)
    - math score (int)
    - reading score (int)
    - writing score (int)
    """
    create_sql = f"""
    CREATE TABLE {TABLE_NAME} (
        "gender"                       STRING,
        "race/ethnicity"              STRING,
        "parental level of education" STRING,
        "lunch"                       STRING,
        "test preparation course"     STRING,
        "math score"                  INT,
        "reading score"               INT,
        "writing score"               INT
    );
    """
    cur.execute(create_sql)


def load_csv_into_table(cur):
    """Load data from the CSV file into the MonetDB table."""
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
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """

    # executemany is fine for this dataset size
    cur.executemany(insert_sql, rows)


def main():
    conn = get_monetdb_connection()
    try:
        cur = conn.cursor()
        drop_table_if_exists(cur)
        create_table(cur)
        load_csv_into_table(cur)
        conn.commit()
        print(f"Successfully created and loaded MonetDB table '{TABLE_NAME}'.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
