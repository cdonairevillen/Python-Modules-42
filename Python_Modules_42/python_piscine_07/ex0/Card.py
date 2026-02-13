from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):

    """
    BHase class for al the subtypes of cards generated for this module.

    Methods:
        - get_card_info(): creates a dictionary for all common info from the
        cards generated.
        - play(): abstract method that will be reimplemented in each card type.
        - is_playable(): common chequer for all cards created for this module.
    """

    def __init__(self, name: str, cost: int, rarity: str) -> None:

        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        pass

    def get_card_info(self) -> Dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
            }

    def is_playable(self, available_mana: int) -> bool:

        playable = True
        if available_mana < self.cost:
            playable = False

        return playable
