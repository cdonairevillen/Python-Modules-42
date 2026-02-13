def mage_counter() -> callable:

    """
    Whith non local variables we can save the information changed between
    calls. static char str -> gnl
    """
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_acumulator(initial_power: int) -> callable:

    """
    We can modify it adding information from out of the fucntion too!
    """
    total_power = initial_power

    def accumulator(add_power: int):
        nonlocal total_power
        total_power += add_power
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:

    """
    As we have seen, we can mix the functionality of two diferent
    functions to achieve a new mixed information.
    """

    def enchant(item_name: str):
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, callable]:

    """
    We can use subsecuent funtions provided to the this main one to
    generate a dictionary with deterministic enties and access to the
    information it keeps inside
    """
    memory = {}

    def store(key: str, value):
        memory[key] = value

    def recall(key: str):
        if key in memory:
            return memory[key]
        return f"Error: {key} not in the vault"

    return {"store": store, "recall": recall}


if __name__ == "__main__":

    print("\nTesting mage counter...")
    try:
        counter = mage_counter()
        i = 1
        while i <= 10:
            print(f"Call {i}", counter())
            i += 1
    except Exception:
        print("Mages are not counting...")

    print()

    print("Testing spell acumulation...")
    try:
        list_acumulated = [50, 10, 5, 1, 3]
        acumulator = spell_acumulator(5)

        for element in list_acumulated:
            print(acumulator(element))

    except Exception:
        print("You coudn't stabilize the acumulament")

    print()

    print("Testing enchantment factory...")
    try:
        fire_enchant = enchantment_factory("Flaming")
        ice_enchant = enchantment_factory("Frozen")

        print(fire_enchant("Sword"))
        print(ice_enchant("Spear"))

    except Exception:
        print("Do you believe in magic?")

    print()

    print("Testing Memory Vault...")
    try:
        vault = memory_vault()
        vault["store"]("hero", "Jace")
        vault["store"]("mana", 100)

        print("Hero enctance:", vault['recall']('hero'))
        print("Mana registered:", vault['recall']('mana'))
        print(vault['recall']('villain'))

    except Exception:
        print("Vault had a problem being generated.")
