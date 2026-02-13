#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Dict
from ex0.Card import Card


class Combatable(ABC):

    """
    Abstract class that implements some of the methods will be used in
    EliteCard and TournamentCard and let the heir to reinterpretate
    """

    @abstractmethod
    def attack(self, target: Card) -> Dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        pass
