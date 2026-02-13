#!/usr/bin/env python3

# This function changes the "unit" information to create a functional print
# with it.
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    if unit == "packets":
        unit = "packets available"
    elif unit == "grams":
        unit = "grams total"
    elif unit == "area":
        unit = "square meters"
    else:
        print("Unknown unit type")
        return

    print(f"{seed_type} seeds: {quantity} {unit}")
