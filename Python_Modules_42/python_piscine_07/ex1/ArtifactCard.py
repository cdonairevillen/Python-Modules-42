from ex0.Card import Card
from typing import Dict


class ArtifactCard(Card):

    """
    Class that inherit from Card and reinterpretate all his functions.

    Methods:
        - get_card_info(): Reconstructs and returns a dictionary with all the
        card entries and adds the creature info to it.
        - play(): Creates a dictionary with te changes generated to the
        game_state by playing the selected card.
        - activate_ability(): generates a new dictionary with all the
        information that can be changed or added to the game_state.
    """
    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        if durability > 0:
            self.effect_type = effect_type
            self.type = "Artifact"
            self.durability = durability
        else:
            raise ValueError

    def get_card_info(self) -> Dict:
        main_info = super().get_card_info()
        main_info["type"] = self.type
        main_info["effect"] = self.effect_type
        main_info["durability"] = self.durability
        return main_info

    def play(self, game_state: Dict) -> Dict:
        played_card = {}

        if super().is_playable(game_state["mana"]) is True:
            game_state["mana"] -= self.cost
            played_card["name"] = self.name
            played_card["mana_used"] = self.cost
            played_card["effect"] = self.effect_type
            return played_card
        else:
            return ("You can not play this card")

    def activate_ability(self) -> Dict:

        ability = {"artifact": self.name,
                   "effect_active": True,
                   "durabililty_left": self.durability,
                   "effect": self.effect_type}

        return ability
