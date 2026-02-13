def spell_combiner(spell1: callable, spell2: callable) -> callable:

    """
    Funtion that combinate the output of the two functions given.
    """
    def combined(*args, **kwargs):
        return f"{spell1(*args, **kwargs)} while {spell2(*args, **kwargs)}"
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:

    """
    This funtion multiplies by 'multiplier' the amount retourned by 'basespell'
    """
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:

    """
    This function uses a function to check if is posible to do other given
    function.
    """
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Failed"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    """
    This function returns a list of all the outpus of the functions called in
    the list given.
    """
    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


if __name__ == "__main__":

    def fireball(target, mana=None):
        return f"Fireball hits {target}"

    def heal(target, mana=None):
        return f"Used Heal on {target}"

    def casteable(target, mana):
        return mana >= 10

    def channel_spell(amount):
        return amount

    print("\nTesting spell combiner...")
    try:
        combo = spell_combiner(fireball, heal)
        print("Combined spell result:", combo("Dragon"))

    except Exception:
        print("You failed to combine both spells")
    print()

    print("\nTesting spell amplifier...")
    try:
        base = 10
        amplified = power_amplifier(channel_spell, 3)
        print(f"Power base: {channel_spell(base)},"
              f" Amplified: {amplified(base)}")

    except Exception:
        print("Your spell blowed up your eyebrows")

    print("\nTesting conditional casting...")
    try:
        conditional = conditional_caster(casteable, fireball)
        print("Low Mana:", conditional("Dragon", 5))
        print("High Mana:", conditional("Dragon", 90))

    except Exception:
        print("Do you even have mana?")

    print("\nTesting Spell Sequence...")
    try:
        sequence = spell_sequence([fireball, heal])
        print("Spell Sequience:", sequence("Goblin"))

    except Exception:
        print("You feel your tonge as a knot")

    print()
