from typing import Dict


class GameEngine():

    """
    Class that manages all the game simulation and information.
    You can configure it with a strategy and a type of factory.

    Methods:
        - configure_engine(): sets the engine to the selected factory and
        strategy
        - simulate_turn(): simulates a turn with a preseted gamestate and hand.
        - get_engine_status(): returns a dictionary with the information setted
        in the game_engine.
    """

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: list,  strategy: list) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:

        hand = [
            self.factory.create_creature("Goblin", 2, "common", 2, 1),
            self.factory.create_spell("Fireball", 3, "common",
                                      "Deals 3 point to target minion")
        ]

        game_state = {
            "mana": 9,
            "targets": ["player",
                        self.factory.create_creature("Goblin", 2,
                                                     "common", 2, 1),
                        self.factory.create_creature("shyvan Dragon", 2,
                                                     "rare", 5, 5),
                        self.factory.create_creature("Young Wolf", 1,
                                                     "common", 1, 1),]
        }

        hand_cards = 0
        enemy_cards = 0
        for cards in hand:
            hand_cards += 1

        for cards in game_state["targets"]:
            if cards == "player":
                continue
            else:
                enemy_cards += 1

        self.cards_created = hand_cards + enemy_cards

        print("Hand:", [card.name + f" ({card.cost})" for card in hand])

        result = self.strategy.execute_turn(hand, game_state)

        self.turns += 1
        self.total_damage += result["damage_dealt"]

        return result

    def get_engine_status(self) -> Dict:

        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
