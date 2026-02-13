from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):

    """
    Abstract class that implements some of the methods will be used in
    TournamentCard and let the heir to reinterpretate
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict:
        pass
