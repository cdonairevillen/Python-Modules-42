#!/usr/bin/env python3

def record_spell(spell_name: str, ingredients: str) -> str:

    """
    Add a new spell to the grimoire dictionary.

    Variables:
        - grimoire: dictionary with all the spells validated

    Functionality:
        - Adds the new sell as a key in the dictionary and the ingredients
        linked to it.

    Returns:
        - Returs a "recorded" string if the spell is correct and a "rejected"
        if is not.
    """

    from .validator import validate_ingredients

    result = validate_ingredients(ingredients)

    grimoire = {}
    if result == "VALID":
        grimoire[spell_name] = ingredients
        return (f" Spell recorded: {spell_name} ({ingredients}) - {result}")
    else:
        return (f" Spell rejected: {spell_name} ({ingredients}) - {result}")
