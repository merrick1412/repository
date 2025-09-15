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

# Merrick Moncure
# Module 3 – Key/Value (pickleDB) Menu App
# Stores one laptop entry per day using pickleDB.

import pickledb
from datetime import date

# ----- database helpers -----
DB_PATH = "laptops.db"          # file where data is saved
DB_AUTOSAVE = True              # save after every write

def get_db():
    return pickledb.load(DB_PATH, DB_AUTOSAVE)  # open or create db

def today_key():
    return date.today().isoformat()             # key is today's date

def has_today_item(db):
    return db.exists(today_key())               # check if today's entry exists

def get_today_item(db):
    return db.get(today_key())                  # fetch today's entry

def set_today_item(db, item_dict):
    db.set(today_key(), item_dict)              # store today's entry

def delete_today_item(db):
    if has_today_item(db):
        db.rem(today_key())                     # remove today's entry

# ----- input validation -----
def get_valid_string(prompt, min_len=5):
    # require at least min_len non-space characters
    while True:
        value = input(prompt)
        if len(value.strip()) < min_len:
            print(f"Error: need at least {min_len} characters.")
        else:
            return value

def get_valid_int(prompt, lo, hi):
    # require integer in given range
    while True:
        try:
            n = int(input(prompt))
            if lo <= n <= hi:
                return n
            print(f"Error: number must be {lo}–{hi}.")
        except ValueError:
            print("Error: enter a whole number.")

def get_valid_float(prompt, lo, hi):
    # require float in given range
    while True:
        try:
            x = float(input(prompt))
            if lo <= x <= hi:
                return x
            print(f"Error: number must be {lo}–{hi}.")
        except ValueError:
            print("Error: enter a real number.")

# ----- menu actions -----
def add_laptop():
    # collect and validate new laptop info
    print("\nAdd Laptop")
    model_name = get_valid_string("Model name (min 5 chars): ", 5)
    ram_gb     = get_valid_int("RAM GB (2–128): ", 2, 128)
    storage_gb = get_valid_int("Storage GB (64–8192): ", 64, 8192)
    screen_in  = get_valid_float("Screen inches (10.0–18.4): ", 10.0, 18.4)
    price_usd  = get_valid_float("Price USD (100–10000): ", 100.0, 10000.0)
    print("\nLaptop saved!\n")
    return {
        "model_name": model_name,
        "ram_gb": ram_gb,
        "storage_gb": storage_gb,
        "screen_in": screen_in,
        "price_usd": price_usd
    }

def edit_laptop(existing):
    # prompt for new values showing current ones
    print("\nEdit Laptop")
    print(f"Current model name: {existing['model_name']}")
    existing["model_name"] = get_valid_string("New model name: ", 5)

    print(f"Current RAM: {existing['ram_gb']} GB")
    existing["ram_gb"] = get_valid_int("New RAM GB (2–128): ", 2, 128)

    print(f"Current Storage: {existing['storage_gb']} GB")
    existing["storage_gb"] = get_valid_int("New Storage GB (64–8192): ", 64, 8192)

    print(f"Current Screen: {existing['screen_in']} in")
    existing["screen_in"] = get_valid_float("New Screen inches (10.0–18.4): ", 10.0, 18.4)

    print(f"Current Price: ${existing['price_usd']}")
    existing["price_usd"] = get_valid_float("New Price USD (100–10000): ", 100.0, 10000.0)

    print("\nLaptop updated!\n")
    return existing

def display_laptop(item):
    # print laptop attributes
    print("\nCurrent Laptop")
    print("--------------")
    print(f"Model name : {item['model_name']}")
    print(f"RAM (GB)   : {item['ram_gb']}")
    print(f"Storage GB : {item['storage_gb']}")
    print(f"Screen (in): {float(item['screen_in']):.1f}")
    print(f"Price (USD): ${float(item['price_usd']):,.2f}\n")

# ----- menu control -----
def menu_choice(valid_letters):
    # loop until user enters a valid menu letter
    valid = [c.upper() for c in valid_letters]
    while True:
        choice = input("Select an option: ").strip().upper()
        if choice in valid:
            return choice
        print(f"Invalid choice. Options: {', '.join(valid)}")

def main():
    db = get_db()
    while True:
        # show correct menu depending on whether today's entry exists
        if not has_today_item(db):
            print("Main Menu\nA) Add Laptop\nQ) Quit")
            choice = menu_choice(["A", "Q"])
            if choice == "A":
                set_today_item(db, add_laptop())
            else:
                print("Goodbye!")
                break
        else:
            print("Main Menu\nA) Edit Laptop\nB) Display Laptop\nD) Delete Laptop\nQ) Quit")
            choice = menu_choice(["A", "B", "D", "Q"])
            if choice == "A":
                set_today_item(db, edit_laptop(get_today_item(db)))
            elif choice == "B":
                display_laptop(get_today_item(db))
            elif choice == "D":
                delete_today_item(db)
                print("Today's laptop entry deleted.\n")
            else:
                print("Goodbye!")
                break

if __name__ == "__main__":
    main()