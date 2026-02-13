try:
    from .spellbook import record_spell
    from .validator import validate_ingredients
except Exception:
    print("This must not be executed, dummy")


if __name__ == "__main__":
    try:
        print(record_spell())
        print(validate_ingredients("air"))
    except Exception:
        print("This must not be executed, dummy")
