#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Dict


class Magical(ABC):

    """
    Abstract class that implements some of the methods will be used in
    EliteCard nd let the heir to reinterpretate
    """

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> Dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        pass
