#!/usr/bin/env python3

import alchemy.elements
from alchemy.elements import create_fire
from alchemy.elements import create_water, create_fire as fire
from alchemy.potions import healing_potion as heal, strength_potion as s

if __name__ == "__main__":

    """
    Prints all the information from the ex1

    """

    print("=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:\n")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print()
    print("Method 2 - Specific function import:\n")
    print("create_water():", create_water())
    print("create_fire():", create_fire())
    print()
    print("Method 3 - Aliased import:")
    print("heal():", heal())
    print()
    print("Method 4 - Multiple imports:")
    print("create_earth():", alchemy.elements.create_earth())
    print("create_fire():", fire())
    print("strength_potion():", s())
