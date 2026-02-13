#!/usr/bin/env python3

from .elements import (create_air, create_earth, create_fire, create_water)


def healing_potion():
    return (f"Healing potion brewed with {create_fire()} and {create_water()}")


def strength_potion():
    return (f"Strength potion brewed with {create_earth()} and"
            f"{create_fire()}")


def invisibility_potion():
    return (f"Invisibility potion brewed with {create_air()} and"
            f"{create_water()}")


def wisdom_potion():
    return ("Wisdom potion brewed with all elements:", create_water(),
            create_earth(), create_air(), create_fire())
