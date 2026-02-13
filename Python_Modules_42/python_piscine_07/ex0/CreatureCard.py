from ex0.Card import Card
from typing import Dict


class CreatureCard(Card):

    """
    Class that inherit from Card and reinterpretate all his functions.

    Methods:
        - get_card_info(): Reconstructs and returns a dictionary with all the
        card entries and adds the creature info to it.
        - play(): Creates a dictionary with te changes generated to the
        game_state by playing the selected card.
        - attack_target(): Simulates a atack from the selected card to the card
        marques as a target
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack >= 0 and health >= 0:
            self.attack = attack
            self.health = health
            self.type = "Creature"
        else:
            raise ValueError

    def get_card_info(self) -> Dict:
        main_info = super().get_card_info()
        main_info["type"] = self.type
        main_info["attack"] = self.attack
        main_info["health"] = self.health
        return main_info

    def play(self, game_state: Dict) -> Dict:

        played_card = {}

        if super().is_playable(game_state["mana"]) is True:
            game_state["mana"] -= self.cost
            played_card["name"] = self.name
            played_card["mana_used"] = self.cost
            played_card["effect"] = "Creature summoned to battlefield"
            return played_card
        else:
            return ("You can not play this card")

    def attack_target(self, target: Card) -> Dict:

        if target.type == "Creature":
            self.health -= target.attack
            target.health -= self.attack

            summary = {
                "attacker": self.name,
                "target": target.name,
                "damage_dealt": self.attack,
                "combat_resolved": True
            }
            return summary
        else:
            return {"combat_resolved": False}
