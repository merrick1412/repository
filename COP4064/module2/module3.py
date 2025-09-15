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
    - User will provide input through the console.
    - All inputs are validated in loops until correct data is entered.
    - Only one Laptop object is managed at a time.
All work below was performed by Merrick Moncure
"""

# ------------------------- Validation --------------------------

def get_valid_string(prompt, min_len=5):
    """Ask until we get a non-empty string with at least min_len chars."""
    while True:
        value = input(prompt)
        # Strip spaces so "     " doesn't count
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
    Attributes (assignment rules):
      - model_name: string, min length 5, not all spaces
      - ram_gb:     int in [2, 128]
      - storage_gb: int in [64, 8192]
      - screen_in:  float in [10.0, 18.4]
      - price_usd:  float in [100.0, 10000.0]
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

def edit_laptop(laptop):
    """
    Edit each attribute. Show current value and let the user either:
      - press Enter to keep it, or
      - type a new value (validated).
    """
    print("\nEdit Laptop\n-----------")

    # Model name
    print(f"Current model name: {laptop['model_name']}")
    new = input("New model name (min 5 chars) or Enter to keep: ")
    if new.strip() != "":
        while len(new.strip()) < 5:
            print("Error: at least 5 non-space characters.")
            new = input("New model name (min 5 chars) or Enter to keep: ")
        laptop["model_name"] = new

    # RAM
    print(f"Current RAM (GB): {laptop['ram_gb']}")
    while True:
        raw = input("New RAM in GB (2..128) or Enter to keep: ")
        if raw == "":
            break
        try:
            val = int(raw)
            if 2 <= val <= 128:
                laptop["ram_gb"] = val
                break
            else:
                print("Error: must be 2..128.")
        except ValueError:
            print("Error: whole number only.")

    # Storage
    print(f"Current Storage (GB): {laptop['storage_gb']}")
    while True:
        raw = input("New Storage in GB (64..8192) or Enter to keep: ")
        if raw == "":
            break
        try:
            val = int(raw)
            if 64 <= val <= 8192:
                laptop["storage_gb"] = val
                break
            else:
                print("Error: must be 64..8192.")
        except ValueError:
            print("Error: whole number only.")

    # Screen size
    print(f"Current Screen (in): {laptop['screen_in']}")
    while True:
        raw = input("New Screen inches (10.0..18.4) or Enter to keep: ")
        if raw == "":
            break
        try:
            val = float(raw)
            if 10.0 <= val <= 18.4:
                laptop["screen_in"] = val
                break
            else:
                print("Error: must be 10.0..18.4.")
        except ValueError:
            print("Error: real number only.")

    # Price
    print(f"Current Price (USD): {laptop['price_usd']}")
    while True:
        raw = input("New Price USD (100.00..10000.00) or Enter to keep: ")
        if raw == "":
            break
        try:
            val = float(raw)
            if 100.0 <= val <= 10000.0:
                laptop["price_usd"] = val
                break
            else:
                print("Error: must be 100.00..10000.00.")
        except ValueError:
            print("Error: real number only.")

    print("\nLaptop updated!\n")

def display_laptop(laptop):
    """Pretty-print the current laptop."""
    print("\nCurrent Laptop")
    print("--------------")
    print(f"Model name : {laptop['model_name']}")
    print(f"RAM (GB)   : {laptop['ram_gb']}")
    print(f"Storage GB : {laptop['storage_gb']}")
    print(f"Screen (in): {laptop['screen_in']:.1f}")
    print(f"Price (USD): ${laptop['price_usd']:,.2f}\n")

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
    laptop = None  # We start with no data saved yet

    while True:
        if laptop is None:
            # Before Add runs
            print("Main Menu")
            print("A) Add Laptop")
            print("Q) Quit")
            choice = menu_choice(["A", "Q"])

            if choice == "A":
                laptop = add_laptop()
            else:
                print("Goodbye!")
                break

        else:
            # After Add has run at least once
            print("Main Menu")
            print("A) Edit Laptop")
            print("B) Display Laptop")
            print("Q) Quit")
            choice = menu_choice(["A", "B", "Q"])

            if choice == "A":
                edit_laptop(laptop)
            elif choice == "B":
                display_laptop(laptop)
            else:
                print("Goodbye!")
                break

if __name__ == "__main__":
    main()