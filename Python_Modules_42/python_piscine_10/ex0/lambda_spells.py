
"""
With lambda you can generate a not deteminated function to work with.
You can modify, compare and save information just using one line of code.
"""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    """
    This fnction returns a list of dicts shorting the elements by their
    power registered.
    """

    result = sorted(artifacts, key=lambda x: x['power'], reverse=True)
    return result


def power_filter(mages: list[dict], min_power: int) -> list[dict]:

    """
    This fuction returns a list of dicts with all the instances in the
    list that goes abobe the tresshold given.
    """

    result = filter(lambda x: x['power'] >= min_power, mages)
    return result


def spell_transformer(spells: list[str]) -> list[str]:

    """
    Transform the elements of the list adding a prefix and sufix using map.
    """

    result = map(lambda x: f"* {x} *", spells)
    return result


def mage_stats(mages: list[dict]) -> dict:

    """
    Compares and creates the average power of all the instanciate object in
    the given list.
    """

    i = 0
    for mage in mages:
        i += 1

    max_power = max(mages, key=lambda x: x['power'])['power']
    min_power = min(mages, key=lambda x: x['power'])['power']
    avg_power = sum(map(lambda x: x['power'], mages)) / i

    result = {
        "max_power": f"{max_power:.2f}",
        "min_power": f"{min_power:.2f}",
        "avg_power": f"{avg_power:.2f}"
    }

    return result


if __name__ == "__main__":

    print("\nTesting artifact sorter...")
    try:

        artifacts_to_sort = [{
            "name": "powerstone",
            "power": 150,
            "type": "artifact"
        },
            {
            "name": "weakstone",
            "power": 50,
            "type": "artifact"
        },
            {
            "name": "fire_staff",
            "power": 76,
            "type": "artifact"
        }]

        sorted_artifacts = artifact_sorter(artifacts_to_sort)
        for artifact in sorted_artifacts:
            print(f"{artifact['name']} ({artifact['power']} power)")
    except Exception:
        print("We have found some issues with the artifacts. Program"
              " continues...")
    print()

    print("Testing power filters...")
    try:
        mages = [{
            "name": "Gregor",
            "power": 7500,
            "element": "Fire"
        }, {
            "name": "julianna",
            "power": 5500,
            "element": "Darkness"
        }, {
            "name": "Boris",
            "power": 2,
            "element": "water"
        }]

        powerfull_mages = power_filter(mages, min_power=500)
        for mage in powerfull_mages:
            print(f"{mage['name']}, ({mage['power']} power)")
    except Exception:
        print("There have been some issues with our mages")
    print()

    print("Testing spell transformer...")
    try:
        spells = ["lightning bolt", "Fireball", "Iceshard"]
        new_spells = spell_transformer(spells)
        for spell in new_spells:
            print(spell)
    except Exception:
        print("Some Spells refused to be transformed")
    print()
    print("Testing mage summary...")
    try:
        summary = mage_stats(mages)
        print(summary)
    except Exception:
        print("I don't really know what could possibly go wrong")
