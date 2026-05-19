"""
Movie Ticket Price Calculator
------------------------------
Calculates the final price of a movie ticket based on age,
seat type, show time, membership status, and weekend pricing.
"""


def get_service_charge(seat_type):
    """
    Return the service charge based on seat type.

    Args:
        seat_type (str): 'Premium', 'Gold', or 'Standard'

    Returns:
        int: Service charge amount
    """
    charges = {
        'Premium': 5,
        'Gold': 3,
        'Standard': 1
    }
    return charges.get(seat_type, 1)


def calculate_ticket_price(age, seat_type, show_time, is_member, is_weekend):
    """
    Calculate the final movie ticket price.

    Args:
        age        (int)  : Age of the user
        seat_type  (str)  : 'Premium', 'Gold', or 'Standard'
        show_time  (str)  : 'Morning', 'Afternoon', or 'Evening'
        is_member  (bool) : Whether the user has a membership
        is_weekend (bool) : Whether it is a weekend

    Returns:
        dict: Breakdown of charges and eligibility info,
              or a string error message if ineligible
    """
    BASE_PRICE = 15

    if age < 18:
        return "Sorry, you must be at least 18 to book a ticket."

    evening_eligible = age >= 21 or is_member
    if show_time == 'Evening' and not evening_eligible:
        return "Sorry, you must be 21+ or a member to book Evening shows."

    discount = 3 if (is_member and age >= 21) else 0
    extra_charges = 2 if (is_weekend or show_time == 'Evening') else 0
    service_charge = get_service_charge(seat_type)
    final_price = BASE_PRICE + extra_charges + service_charge - discount

    return {
        "base_price":     BASE_PRICE,
        "seat_type":      seat_type,
        "service_charge": service_charge,
        "extra_charges":  extra_charges,
        "discount":       discount,
        "final_price":    final_price
    }


def display_ticket(result):
    """Print a formatted ticket price breakdown."""
    if isinstance(result, str):
        print(f"\n  {result}\n")
        return

    print("=" * 40)
    print("     MOVIE TICKET PRICE BREAKDOWN")
    print("=" * 40)
    print(f"  Base price       : ${result['base_price']}")
    print(f"  Seat ({result['seat_type']:>8})  : +${result['service_charge']}")
    print(f"  Extra charges    : +${result['extra_charges']}")
    print(f"  Membership disc. : -${result['discount']}")
    print("-" * 40)
    print(f"  Final price      : ${result['final_price']}")
    print("=" * 40)


# --- Run the calculator ---
if __name__ == "__main__":
    result = calculate_ticket_price(
        age=21,
        seat_type='Premium',
        show_time='Morning',
        is_member=True,
        is_weekend=False
    )
    display_ticket(result)