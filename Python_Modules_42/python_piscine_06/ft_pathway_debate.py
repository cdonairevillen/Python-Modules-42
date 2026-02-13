#!/usr/bin/env python3

import alchemy.transmutation.basic as Basic
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life
from alchemy.transmutation import (lead_to_gold as gold,
                                   philosophers_stone as stone)

if __name__ == "__main__":

    """
    Prints all the information from the ex2

    """

    print("=== Pathway Debate Mastery ===")
    print()
    print("Testing Absolute Imports (from basic.py):")
    print("lead_to_gold():", Basic.lead_to_gold())
    print("stone_to_gem():", Basic.stone_to_gem())
    print()
    print("Testing Relative Imports (from advanced.py):")
    print("philosophers_stone():", philosophers_stone())
    print("elixir_of_life()", elixir_of_life())
    print()
    print("Testing Package Access:")
    print("alchemy.transmutation.lead_to_gold():", gold())
    print("alchemy.transmutation.philosophers_stone()", stone())
    print()
    print("Both pathways work! Absolute: clear, Relative: concise")
