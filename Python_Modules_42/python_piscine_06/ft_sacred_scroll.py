#!/usr/bin/env python3
import alchemy as a
from alchemy import create_fire, create_water
from alchemy.elements import (create_air as air, create_water as water,
                              create_fire as fire, create_earth as earth)

if __name__ == "__main__":

    """
    Prints all the information from the ex0

    """

    element_list = [fire(), water(), earth(), air()]

    print("== Sacred Scroll Mastery ===\n")
    print("\nTesting direct module access:")
    for element in element_list:
        try:
            print(f"alchemy.elements.create_{element}(): ", element)

        except AttributeError:
            print("AttributeError - not exposed")

    print()
    print("\nTesting package-level access (controled by __init__.py):")
    try:
        print("alchemy.create_fire():", create_fire())
    except AttributeError as e:
        print(f"create_fire(): {e} - not exposed")
    try:
        print("alchemy.create_water():", create_water())
    except AttributeError as e:
        print(f"create_water(): {e} - not exposed")
    try:
        print("alchemy.create_earth():", a.create_earth())
    except AttributeError as e:
        print(f"create_earth(): {e} - not exposed")
    try:
        print("alchemy.create_air():", a.create_air())
    except AttributeError as e:
        print(f"create_air(): {e} - not exposed")

    print("\nPackage metadata:")
    print("Version:", a.__version__)
    print("Author:", a.__author__)
