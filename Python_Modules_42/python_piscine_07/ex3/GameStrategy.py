from abc import ABC, abstractmethod
from typing import Dict


class GameStrategy(ABC):

    """
    Abstract class that implements some of the methods will be used in
    AgresiveStrategy and let the heir to reinterpretate.
    """

    @abstractmethod
    def execute_turn(self, hand: list, game_state: Dict) -> Dict:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def priorize_targets(self, available_targets: list) -> list:
        pass
