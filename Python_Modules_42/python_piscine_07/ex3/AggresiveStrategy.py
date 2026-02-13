from typing import Dict
from ex3.GameStrategy import GameStrategy


class AgresiveStrategy(GameStrategy):

    """
    Class that inherit from Gamestrategy and reinterpretate all his functions.

    Methods:
        - get_strategy_name(): returns the name of the strategy called.
        - priorize_targets(): creates a target list that looks for plausible
        objetives to win the gameboard.
        - execute_turn(): Simulates a turn dependent of the data and strategy
        used.
    """

    def get_strategy_name(self) -> str:
        return "AgresiveStrategy"

    def priorize_targets(self, available_targets: list) -> list:

        target_list = []
        for target in available_targets:
            if target == "player":
                target_list = target_list + [target]

        for target in available_targets[1:]:
            if target.health < 2:
                target_list = target_list + [target.name]

        return target_list

    def execute_turn(self, hand: list, game_state: Dict) -> Dict:
        cards_played = []
        mana_used = 0
        damage = 0

        for card in hand:
            if card.cost > game_state["mana"]:
                continue
            cards_played = cards_played + [card.name]
            game_state["mana"] -= card.cost
            mana_used += card.cost

            if card.type == "Creature":
                damage += card.attack

            elif card.type == "Spell":
                if card.effect == "Deals 3 point to target minion":
                    damage += 3

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "damage_dealt": damage,
            "targets_attacked": self.priorize_targets(game_state["targets"])
        }
