from ex0.Card import Card
from typing import Dict


class SpellCard(Card):

    """
    Class that inherit from Card and reinterpretate all his functions.

    Methods:
        - get_card_info(): Reconstructs and returns a dictionary with all the
        card entries and adds the creature info to it.
        - play(): Creates a dictionary with te changes generated to the
        game_state by playing the selected card.
        - attack_target(): generates a effect in the selected target/s
        depending of the effect the spell has.
    """
    def __init__(self, name: str, cost: int,
                 rarity: str, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect = effect
        self.type = "Spell"
        self.uses = 1

    def get_card_info(self) -> Dict:
        main_info = super().get_card_info()
        main_info["type"] = self.type
        main_info["effect"] = self.effect
        main_info["uses"] = self.uses
        return main_info

    def play(self, game_state: Dict) -> Dict:
        played_card = {}

        if super().is_playable(game_state["mana"]) is True:
            game_state["mana"] -= self.cost
            played_card["name"] = self.name
            played_card["mana_used"] = self.cost
            played_card["effect"] = self.effect
            return played_card
        else:
            return ("You can not play this card")

    def resolve_effect(self, targets: list) -> Dict:

        len = 0
        creature_count = 0
        artifact_count = 0
        for target in targets:
            len += 1
            if target.type == "Creature":
                creature_count += 1
            elif target.type == "Artifact":
                artifact_count += 1

        if len == 1:
            if targets[0].type == "Creature":
                if self.effect == "Heal 3 point to target minion":
                    targets[0].health += 3
                elif self.effect == "Deals 3 point to target minion":
                    targets[0].health -= 3
                elif self.effect == "Gives your minion +3 attack":
                    targets[0].attack += 3
                self.uses -= 1
            elif targets.type == "Artifact":
                if self.effect == "Destroy target artifact":
                    targets[0].durbility = 0
                self.uses -= 1
            else:
                return ("Not valid target for this spell")

        else:
            if len == creature_count:
                if (self.effect == "Give 3 target minions +1 attack"):
                    for creature in targets:
                        creature.attack += 1
                elif self.effect == "Deal 2 damage to 2 target minions":
                    for creature in targets:
                        creature.health -= 2
                self.uses -= 1
            elif len == artifact_count:
                if (self.effect == "Take 1 durability"
                   "to 2 target artifacts"):
                    for artifact in targets:
                        artifact.durability -= 1
                self.uses -= 1
            else:
                return ("Not valid targets for this spell")
