"""
Name: Merrick Moncure
Date: 11/30/2025
Assignment: Column Store Project – Part 1 (CreateMergedDB.py)
Due Date: 11/30/2025

About this script:
- Creates an updatable MERGE TABLE in MonetDB partitioned by items_count
- Child tables are partitioned by RANGE on items_count
- Loads partition tables from the base fast_food_orders table
"""

import pymonetdb

MONETDB_HOST = "localhost"
MONETDB_PORT = 50000
MONETDB_USER = "monetdb"
MONETDB_PASSWORD = "monetdb"
MONETDB_DATABASE = "demo"

BASE_TABLE = "fast_food_orders"
MERGE_TABLE = "fast_food_orders_merged"

PART_TABLE_SMALL = "fast_food_orders_small"   # items_count 1–3
PART_TABLE_MED   = "fast_food_orders_medium"  # items_count 4–6
PART_TABLE_LARGE = "fast_food_orders_large"   # items_count 7+


def get_connection():
    return pymonetdb.connect(
        username=MONETDB_USER,
        password=MONETDB_PASSWORD,
        hostname=MONETDB_HOST,
        port=MONETDB_PORT,
        database=MONETDB_DATABASE,
    )


def drop_existing_tables():
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(f"DROP TABLE IF EXISTS {MERGE_TABLE} CASCADE;")
        cur.execute(f"DROP TABLE IF EXISTS {PART_TABLE_SMALL} CASCADE;")
        cur.execute(f"DROP TABLE IF EXISTS {PART_TABLE_MED} CASCADE;")
        cur.execute(f"DROP TABLE IF EXISTS {PART_TABLE_LARGE} CASCADE;")
        conn.commit()
    finally:
        cur.close()
        conn.close()


def create_partition_tables_and_merge():
    ddl_part = f"""
        (
            order_id               VARCHAR(32) PRIMARY KEY,
            order_time             TIMESTAMP,
            city                   VARCHAR(64),
            cuisine_type           VARCHAR(64),
            order_value            DECIMAL(10,2),
            delivery_time_minutes  INT,
            payment_method         VARCHAR(64),
            items_count            INT
        )
    """

    conn = get_connection()
    cur = conn.cursor()
    try:
        # Child partition tables
        cur.execute(f"CREATE TABLE {PART_TABLE_SMALL} {ddl_part};")
        cur.execute(f"CREATE TABLE {PART_TABLE_MED} {ddl_part};")
        cur.execute(f"CREATE TABLE {PART_TABLE_LARGE} {ddl_part};")

        # MERGE TABLE partitioned by RANGE on items_count (integer column)
        cur.execute(
            f"""
            CREATE MERGE TABLE {MERGE_TABLE} {ddl_part}
            PARTITION BY RANGE ON (items_count);
            """
        )

        # Attach child tables as partitions with non-overlapping ranges
        cur.execute(
            f"""
            ALTER TABLE {MERGE_TABLE}
            ADD TABLE {PART_TABLE_SMALL}
            AS PARTITION FROM RANGE MINVALUE TO 4;
            """
        )
        cur.execute(
            f"""
            ALTER TABLE {MERGE_TABLE}
            ADD TABLE {PART_TABLE_MED}
            AS PARTITION FROM 4 TO 7;
            """
        )
        cur.execute(
            f"""
            ALTER TABLE {MERGE_TABLE}
            ADD TABLE {PART_TABLE_LARGE}
            AS PARTITION FROM 7 TO RANGE MAXVALUE;
            """
        )

        conn.commit()
    finally:
        cur.close()
        conn.close()


def populate_partitions_from_base():
    conn = get_connection()
    cur = conn.cursor()
    try:
        # Small orders: items_count < 4
        cur.execute(
            f"""
            INSERT INTO {PART_TABLE_SMALL}
            SELECT *
            FROM {BASE_TABLE}
            WHERE items_count IS NOT NULL AND items_count < 4;
            """
        )

        # Medium orders: 4 <= items_count < 7
        cur.execute(
            f"""
            INSERT INTO {PART_TABLE_MED}
            SELECT *
            FROM {BASE_TABLE}
            WHERE items_count >= 4 AND items_count < 7;
            """
        )

        # Large orders: items_count >= 7
        cur.execute(
            f"""
            INSERT INTO {PART_TABLE_LARGE}
            SELECT *
            FROM {BASE_TABLE}
            WHERE items_count >= 7;
            """
        )

        conn.commit()
    finally:
        cur.close()
        conn.close()


def main():
    drop_existing_tables()
    create_partition_tables_and_merge()
    populate_partitions_from_base()
    print(f"Created merge table '{MERGE_TABLE}' with range partitions on items_count.")


if __name__ == "__main__":
    main()
