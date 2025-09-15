"""
Name: Merrick Moncure
Date: 9/14/2025
Assignment: Module 3 – Key/Value (pickleDB) Menu App
Due Date: 9/14/25
About this project:
    This project is a menu-driven Python program that lets the user
    add, edit, and display information about a Laptop.
    The project demonstrates input validation loops,
    range checking, and menu control flow.
Assumptions:
- Stores one "Laptop" object per day in pickleDB.
- Key is today's date "YYYY-MM-DD".
- Implements Add/Edit/Display/Delete with input-validation loops.
All work below was performed by Merrick Moncure
"""

import pickledb
from datetime import date

# ------------------------- Persistence -------------------------

DB_PATH = "laptops.db"          # the pickleDB file on disk
DB_AUTOSAVE = True              # flush after every write

def get_db():
    # Opens or creates the db file
    return pickledb.load(DB_PATH, DB_AUTOSAVE)

def today_key() -> str:
    return date.today().isoformat()   # e.g., "2025-09-06"

def has_today_item(db) -> bool:
    return db.exists(today_key())

def get_today_item(db):
    return db.get(today_key())

def set_today_item(db, item_dict):
    db.set(today_key(), item_dict)

def delete_today_item(db):
    if has_today_item(db):
        db.rem(today_key())

# ------------------------- Validation --------------------------

def get_valid_string(prompt, min_len=5):
    """Ask until we get a non-empty string with at least min_len chars."""
    while True:
        value = input(prompt)
        if len(value.strip()) < min_len:
            print(f"Error: please enter at least {min_len} non-space characters.")
        else:
            return value

def get_valid_int(prompt, lo, hi):
    """Ask until we get an int in [lo, hi]."""
    while True:
        raw = input(prompt)
        try:
            n = int(raw)
        except ValueError:
            print("Error: enter a whole number (e.g., 8).")
            continue
        if not (lo <= n <= hi):
            print(f"Error: number must be between {lo} and {hi}.")
            continue
        return n

def get_valid_float(prompt, lo, hi):
    """Ask until we get a float in [lo, hi]."""
    while True:
        raw = input(prompt)
        try:
            x = float(raw)
        except ValueError:
            print("Error: enter a real number (decimals allowed).")
            continue
        if not (lo <= x <= hi):
            print(f"Error: number must be between {lo} and {hi}.")
            continue
        return x

# ------------------------- App Logic ---------------------------

def add_laptop():
    """
    Create a laptop dict after validating each field.
    Attributes (meets assignment rules):
      - model_name: string, min length 5, not all spaces
      - ram_gb:     int in [2, 128]           (whole number w/ range)
      - storage_gb: int in [64, 8192]         (whole number w/ range)
      - screen_in:  float in [10.0, 18.4]     (real number w/ range)
      - price_usd:  float in [100.0, 10000.0] (real number w/ range)
    """
    print("\nAdd Laptop\n----------")
    model_name = get_valid_string("Model name (min 5 chars): ", 5)
    ram_gb     = get_valid_int("RAM in GB (2..128): ", 2, 128)
    storage_gb = get_valid_int("Storage in GB (64..8192): ", 64, 8192)
    screen_in  = get_valid_float("Screen size inches (10.0..18.4): ", 10.0, 18.4)
    price_usd  = get_valid_float("Price USD (100.00..10000.00): ", 100.0, 10000.0)

    print("\nLaptop saved!\n")
    return {
        "model_name": model_name,
        "ram_gb": ram_gb,
        "storage_gb": storage_gb,
        "screen_in": screen_in,
        "price_usd": price_usd
    }

def edit_laptop(existing):
    """
    Edit each attribute. Show current value and require a valid replacement.
    (Enter is NOT accepted here—per spec we prompt until the new value is valid.)
    """
    print("\nEdit Laptop\n-----------")

    print(f"Current model name: {existing['model_name']}")
    existing["model_name"] = get_valid_string("New model name (min 5 chars): ", 5)

    print(f"Current RAM (GB): {existing['ram_gb']}")
    existing["ram_gb"] = get_valid_int("New RAM in GB (2..128): ", 2, 128)

    print(f"Current Storage (GB): {existing['storage_gb']}")
    existing["storage_gb"] = get_valid_int("New Storage in GB (64..8192): ", 64, 8192)

    print(f"Current Screen (in): {existing['screen_in']}")
    existing["screen_in"] = get_valid_float("New Screen inches (10.0..18.4): ", 10.0, 18.4)

    print(f"Current Price (USD): {existing['price_usd']}")
    existing["price_usd"] = get_valid_float("New Price USD (100.00..10000.00): ", 100.0, 10000.0)

    print("\nLaptop updated!\n")
    return existing

def display_laptop(item):
    """Pretty-print the current laptop."""
    print("\nCurrent Laptop")
    print("--------------")
    print(f"Model name : {item['model_name']}")
    print(f"RAM (GB)   : {item['ram_gb']}")
    print(f"Storage GB : {item['storage_gb']}")
    print(f"Screen (in): {float(item['screen_in']):.1f}")
    print(f"Price (USD): ${float(item['price_usd']):,.2f}\n")

# --------------------------- Menu ------------------------------

def menu_choice(valid_letters):
    """Ask for a single-letter menu choice until it's valid."""
    valid = [c.upper() for c in valid_letters]
    while True:
        choice = input("Select an option: ").strip().upper()
        if choice in valid:
            return choice
        print(f"Invalid choice. Options: {', '.join(valid)}")

def main():
    db = get_db()

    while True:
        # Show the correct menu based on whether today's item exists
        if not has_today_item(db):
            print("Main Menu")
            print("A) Add  Laptop")
            print("Q) Quit")
            choice = menu_choice(["A", "Q"])

            if choice == "A":
                item = add_laptop()
                set_today_item(db, item)   # persist to pickledb
            else:
                print("Goodbye!")
                break

        else:
            print("Main Menu")
            print("A) Edit    Laptop")
            print("B) Display Laptop")
            print("D) Delete  Laptop")
            print("Q) Quit")
            choice = menu_choice(["A", "B", "D", "Q"])

            if choice == "A":
                current = get_today_item(db)
                updated = edit_laptop(current)
                set_today_item(db, updated)
            elif choice == "B":
                display_laptop(get_today_item(db))
            elif choice == "D":
                delete_today_item(db)
                print("Today's laptop entry has been deleted.\n")
            else:
                print("Goodbye!")
                break

if __name__ == "__main__":
    main()