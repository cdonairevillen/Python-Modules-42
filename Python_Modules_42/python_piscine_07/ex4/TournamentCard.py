from ex4.Rankable import Rankable
from ex2.Combatable import Combatable
from ex0.Card import Card
from typing import Dict
import random


class TournamentCard(Card, Combatable, Rankable):

    """
    Class that generates a TournamentCard inherit from Card, Combatable and
    Rankeable.

    Methods:
        - play(): Creates a dictionary with te changes generated to the
        game_state by playing the selected card.
        - attack(): Simulates a atack from the selected card to the card
        marques as a target.
        - defend(): Simulates a damage reception and a block effect.
        - get_combat_stats(): returns a dictionary of all the melee combat
        information.
        - update_wins(): update the wins information of the card.
        - update_losses(): update the losses information of the card.
        - combat_status(): returns a dictionary with the information of the
        combat in certain point.
        - calculate_rating(): calculate the rank of the card dependeing of the
        wins and losses achieved.
        - get_tournament_stats(): returns a dictionary with the information
        setted in the game_engine.
    """

    def __init__(self, name: str, cost: int,
                 rarity: str, damage: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if damage >= 0 and health >= 0:
            self.damage = damage
            self.health = health
            self.type = "TournamentCard"
            self.wins = 0
            self.losses = 0
            self.rating = 1200
        else:
            raise ValueError

    def play(self, game_state: Dict) -> Dict:
        if self.cost <= game_state["mana"]:
            game_state["mana"] -= self.cost
            return {
                "name": self.name,
                "mana_used": self.cost,
                "effect": "Tournament card played"
            }
        return ("You can not play this card")

    def attack(self, target: Card) -> Dict:
        chance = random.randint(1, 4)
        if chance > 1:
            damage_dealt = 0
        else:
            damage_dealt = self.damage
        target.health -= damage_dealt
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": damage_dealt,
            "target_health": target.health
        }

    def calculate_rating(self) -> int:
        return 1200 + (self.wins * 16) - (self.losses * 16)

    def get_tournament_stats(self) -> Dict:
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.rating
        }

    def get_rank_info(self) -> Dict:
        rank_info = {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

        return rank_info

    def defend(self, incoming_damage: int) -> Dict:
        self.health -= incoming_damage
        return {"defender": self.name,
                "damage_taken": incoming_damage,
                "remaining_health": self.health}

    def get_combat_stats(self) -> Dict:
        return {"name": self.name,
                "health": self.health,
                "damage": self.damage}

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
