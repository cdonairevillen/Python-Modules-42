import functools as ft
import time


def spell_timer(func: callable) -> callable:
    """
    This function adds a time control to the functions who is attached.
    ft.wraps preserve the metadata of the original function when is
    enveloped with the decorator.
    """
    @ft.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        tic = time.time()
        result = func(*args, **kwargs)
        tac = time.time()
        print(f"Spell completed in {tac - tic:.2f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:

    """
    This funtion provides a int validator to the functions who is
    decorating.
    """
    def decorator(func: callable) -> callable:
        @ft.wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) > 1:
                power = args[2]
            else:
                power = args[0]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attemps: int) -> callable:

    """
    This function generates a decoratos that provides a error control
    to the functions who is added to
    """
    def decorator(func: callable) -> callable:
        @ft.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attemps:
                try:
                    return func(*args, **kwargs)

                except Exception:
                    attempts += 1
                    if attempts < max_attemps:
                        print("Spell Failed, retraying..."
                              f" (attempt {attempts})")
            return f"Spell casting failed after {max_attemps} attempts"
        return wrapper
    return decorator


class MageGuild:

    """
    This function contain the static method to check the wizard name
    and cast_spell, a function modified by a custom decorator to provide
    a external checker for the power given to the function.
    """

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if isinstance(name, str) and len(name) >= 3:
            for char in name:
                if char.isnumeric():
                    return False
        return True

    @power_validator(10)
    @retry_spell(5)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    @spell_timer
    def pyroblast():
        time.sleep(5)
        return "Piroblast cast!"

    @retry_spell(5)
    @spell_timer
    def chaos_orb():
        time.sleep(0.3)
        raise Exception("BOOM!")

    print("\nTesting spell timer...")
    result = pyroblast()
    print("Result:", result)

    print()
    print("Testing Retry Spell...")
    print(chaos_orb())

    print()

    print("Testing Mageguild...")
    print("Curonos name:", MageGuild.validate_mage_name("Cunoros"))
    print("X21 name:", MageGuild.validate_mage_name("X21"))

    guild = MageGuild()
    print(guild.cast_spell("lightning Bolt", 15))
    print(guild.cast_spell("Frost Ball", 5))
