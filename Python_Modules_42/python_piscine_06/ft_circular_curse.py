#!/usr/bin/env python3

import alchemy.grimoire.spellbook as Spellbook
from alchemy.grimoire.spellbook import record_spell as record
from alchemy.grimoire.validator import validate_ingredients

if __name__ == "__main__":

    """
    Prints all the information from the ex3

    """

    print("=== Circular Curse Breaking ===")
    print()
    print("Testing ingredients validation:")
    print("validate_ingredients('fire air'): fire air -",
          validate_ingredients("fire air"))
    print("validate_ingredients('dragon scales'): dragon scales -",
          validate_ingredients("fire air"))
    print()
    print("Testing spell recording with validation:")
    print("record_spell('Fireball', 'fire air'):",
          record("Fireball", "fire air"))
    print("record_spell('Dark Magic', 'shadow'):",
          record("Dark Magic", "shadow"))
    print()
    print("Testing late import technique:")
    print("record_spell('Lightning', 'air'):",
          Spellbook.record_spell("Lightning", "air"))
    print()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
