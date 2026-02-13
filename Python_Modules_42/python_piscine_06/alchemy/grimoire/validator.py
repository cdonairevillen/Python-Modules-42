#!/usr/bin/env python3

def validate_ingredients(ingredients: str) -> str:

    """
    Validates the ingredients of the spells requested to
    add to grimoire

    Variables:
        - usable: Bolean that checks if the spell is valid in all
        the parameters

    Functionality:
        - Checks the list of valid ingridients and the list linked from
        "spellbook". If there is anything diferent from the list, it returns
        invalid

    Returns:
        - Returns "VALID" if the ingredients are correct and invalid if any
        of the ingredients is not in the valid ingredients.
    """

    valid_ingredients = ["fire", "water", "earth", "air"]
    assets = ingredients.split(" ")
    usable = True
    for asset in assets:
        if asset not in valid_ingredients:
            usable = False

    if usable is True:
        return ("VALID")
    else:
        return ("INVALID")
