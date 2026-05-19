"""
Number Base Converter
----------------------
Converts numbers between different bases:
  - Decimal to Binary, Octal, and Hexadecimal
  - Binary, Octal, or Hexadecimal back to Decimal
"""


def decimal_to_all(num):
    """
    Convert a decimal number to binary, octal, and hexadecimal.

    Args:
        num (int): A non-negative decimal integer

    Returns:
        dict: Conversion results in all three bases
    """
    return {
        "decimal":     num,
        "binary":      bin(num)[2:],
        "octal":       oct(num)[2:],
        "hexadecimal": hex(num)[2:].upper()
    }


def to_decimal(value, base):
    """
    Convert a number from a given base to decimal.

    Args:
        value (str): The number as a string (e.g. '11111111')
        base  (int): The base to convert from (2, 8, or 16)

    Returns:
        int: The decimal equivalent
    """
    return int(value, base)


def display_results(result):
    """Print a formatted conversion table."""
    print("=" * 38)
    print("       BASE CONVERSION RESULTS")
    print("=" * 38)
    print(f"  Decimal     : {result['decimal']}")
    print(f"  Binary      : {result['binary']}")
    print(f"  Octal       : {result['octal']}")
    print(f"  Hexadecimal : {result['hexadecimal']}")
    print("=" * 38)


def get_menu_choice():
    """Display menu and return the user's choice."""
    print("\n" + "=" * 38)
    print("       NUMBER BASE CONVERTER")
    print("=" * 38)
    print("  1. Decimal → Binary, Octal, Hex")
    print("  2. Binary  → Decimal")
    print("  3. Octal   → Decimal")
    print("  4. Hex     → Decimal")
    print("  5. Exit")
    print("=" * 38)
    return input("  Enter your choice (1-5): ").strip()


def run():
    """Main loop — keeps the program running until user exits."""
    base_map = {
        "2": ("Binary",      2),
        "3": ("Octal",       8),
        "4": ("Hexadecimal", 16)
    }

    while True:
        choice = get_menu_choice()

        if choice == "1":
            try:
                num = int(input("\n  Enter a decimal number: "))
                if num < 0:
                    print("  Please enter a non-negative number.")
                else:
                    display_results(decimal_to_all(num))
            except ValueError:
                print("  Invalid input. Please enter a whole number.")

        elif choice in base_map:
            name, base = base_map[choice]
            value = input(f"\n  Enter a {name} number: ").strip()
            try:
                result = to_decimal(value, base)
                print(f"\n  {name} {value} = {result} in Decimal")
            except ValueError:
                print(f"  Invalid {name} number.")

        elif choice == "5":
            print("\n  Goodbye!\n")
            break

        else:
            print("  Invalid choice. Please enter a number between 1 and 5.")


# --- Run the program ---
if __name__ == "__main__":
    run()