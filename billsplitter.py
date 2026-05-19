"""
Bill Splitter
-------------
Calculates how much each person owes
after splitting a restaurant bill with tip.
"""

def split_bill(num_friends, tip_percent, *item_costs):
    """
    Calculate the amount each person pays.

    Args:
        num_friends  (int)   : Number of people splitting the bill
        tip_percent  (float) : Tip percentage (e.g. 25 for 25%)
        *item_costs  (float) : Variable number of bill items

    Returns:
        dict: Breakdown of bill details
    """
    subtotal = sum(item_costs)
    tip_amount = subtotal * (tip_percent / 100)
    total_with_tip = subtotal + tip_amount
    per_person = round(total_with_tip / num_friends, 2)

    return {
        "subtotal": subtotal,
        "tip_amount": tip_amount,
        "total": total_with_tip,
        "per_person": per_person
    }


def display_bill(result):
    """Print a formatted bill summary."""
    print("=" * 35)
    print("        BILL SUMMARY")
    print("=" * 35)
    print(f"  Subtotal     : ${result['subtotal']:.2f}")
    print(f"  Tip          : ${result['tip_amount']:.2f}")
    print(f"  Total        : ${result['total']:.2f}")
    print("-" * 35)
    print(f"  Each person  : ${result['per_person']:.2f}")
    print("=" * 35)


# --- Run the bill splitter ---
if __name__ == "__main__":
    bill = split_bill(
        4,       # number of friends
        25,      # tip percentage
        37.89,   # appetizers
        57.34,   # main courses
        39.39,   # desserts
        64.21    # drinks
    )
    display_bill(bill)