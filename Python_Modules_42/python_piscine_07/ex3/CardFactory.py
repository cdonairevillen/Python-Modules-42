from abc import ABC, abstractmethod
from ex0.Card import Card
from typing import Dict


class CardFactory(ABC):

    """
    Abstract class that implements some of the methods will be used in
    FanstasyCardFactory and let the heir to reinterpretate
    """

    @abstractmethod
    def create_creature(self, name: str, cost: int, rarity: str,
                        attack: int, health: int) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name: str, cost: int,
                     rarity: str, effect: str) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name: str, cost: int, rarity: str,
                        durability: int, effect: str) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict:
        pass
