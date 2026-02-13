import functools as ft
import operator


def spell_reducer(spells: list[int], operation: str) -> int:

    """
    Uses functools and operator to check the values of the elements
    provided in the list.
    """

    if operation == "add":
        result = ft.reduce(operator.add, spells)
    elif operation == "multiply":
        result = ft.reduce(operator.mul, spells)
    elif operation == "max":
        result = ft.reduce(lambda a, b: a if a > b else b, spells)
    elif operation == "min":
        result = ft.reduce(lambda a, b: a if a < b else b, spells)

    return result


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:

    """
    ft.partial let us to inicialize functions with just part of the imput
    provided, setting some information based inside the current funtion.
    """
    fire = ft.partial(base_enchantment, power=50, element="Fire")
    ice = ft.partial(base_enchantment, power=10, element="Ice")
    dark = ft.partial(base_enchantment, power=70, element="Darkness")

    return {"fire_enchant": fire,
            "ice_enchant": ice,
            "darkness_enchant": dark}


@ft.lru_cache(maxsize=None)
def memorized_fibonacci(n: int) -> int:

    """
    the decorator ft.lru_cache saves the subsecuents calls into the cache
    mantaining the information setted by the program to make this own calls
    faster.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memorized_fibonacci(n-1) + memorized_fibonacci(n-2)


def spell_dispatcher() -> callable:

    """
    ft.singledispatch generate some temporal register funtions that will
    check for the imput type gived to the funtion and interpretate it
    depending of that type.
    """
    @ft.singledispatch
    def cast(spell):
        return f"Unknown spell type: {type(spell)}"

    @cast.register
    def _(damage: int):
        return f"Deals {damage} points of damage."

    @cast.register
    def _(enchant: str):
        return f"Applies {enchant} to your weapon."

    @cast.register
    def _(spells: list):
        result = [cast(s) for s in spells]
        return result

    return cast


if __name__ == "__main__":

    def enchant(power: int, element: str, target: str):
        return f"{element} enchantment hits {target} with {power} damage"

    print("\nTesting Spell reducer...")
    try:
        list_of_num = [50, 3, 41, 22, 5]
        print("Sum:", spell_reducer(list_of_num, "add"))
        print("Product:", spell_reducer(list_of_num, "multiply"))
        print("Max:", spell_reducer(list_of_num, "max"))
        print("Min:", spell_reducer(list_of_num, "min"))

    except Exception:
        print("How about math?")

    print()

    print("Testing Partial enchanter...")
    try:
        enchanter = partial_enchanter(enchant)

        print("Used", enchanter["fire_enchant"](target="Dragon"))
        print("Used", enchanter["ice_enchant"](target="Goblin"))
        print("Used", enchanter["darkness_enchant"](target="Gnoll"))

    except Exception:
        print("Just too lazy to write it all")

    print()

    print("Testing Memorized Fibonacci...")
    try:

        print("Fibo(10):", memorized_fibonacci(10))
        print("Fibo(15):", memorized_fibonacci(15))
        print("Fibo(50):", memorized_fibonacci(50))

    except Exception:
        print("Bouhu... You don't know fibonacci")

    print()

    print("Testing Spell dispatcher...")
    try:
        dispatcher = spell_dispatcher()

        print(dispatcher(10))
        print(dispatcher("Fire"))
        print(dispatcher([5, "Ice", 20]))

    except Exception:
        print("Dispatch... what a cool game")
