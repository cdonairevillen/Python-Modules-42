from typing import Dict
from ex4.TournamentCard import TournamentCard


class TournamentPlatform():

    """
    Class that generates an interface.

    Methods:
        - register_card(): register a TournamentCard to the self.cards
        dictionary
        - create_match(): Generated an interaction between the 2 contendents.
        They fight and actualize the information from the tournament when any
        of them loses.
        - get_leaderboard(): prints the actual laderboard of the game.
        - generate_tournament_report(): returns a dctionary of all the
        information of the stats of the tounament.
    """

    def __init__(self):
        self.counter = 0
        self.cards = {}
        self.matches_played = 0
        self.interfaces = ["Card", "Combatable", "Rankable"]

    def register_card(self, card: TournamentCard) -> str:

        self.counter += 1
        card_id = card.name + "_" + f"{self.counter}"

        self.cards[card_id] = card

        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        base_card1 = card1.health
        base_card2 = card2.health

        while card1.health > 0 and card2.health > 0:
            card1.attack(card2)
            if card2.health <= 0:
                break
            card2.attack(card1)

        if card1.health > 0:
            winner = card1
            loser = card2
            winner_id = card1_id
            loser_id = card2_id

        else:
            winner = card2
            loser = card1
            winner_id = card2_id
            loser_id = card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        winner.rating = winner.calculate_rating()
        loser.rating = loser.calculate_rating()

        self.matches_played += 1

        card1.health = base_card1
        card2.health = base_card2

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        combat_cards = []
        for card in self.cards.values():
            combat_cards = combat_cards + [card]

        laderboard = []

        while combat_cards:
            best_card = combat_cards[0]

            for card in combat_cards:
                if card.rating > best_card.rating:
                    best_card = card

            laderboard = laderboard + [{"name": best_card.name,
                                        "rating": best_card.rating,
                                        "wins": best_card.wins,
                                        "losses": best_card.losses}]

            combat_cards.remove(best_card)

        return laderboard

    def generate_tournament_report(self) -> dict:
        total_cards = 0
        total_rating = 0

        for card in self.cards.values():
            total_cards += 1
            total_rating += card.rating

        if total_cards > 0:
            avg_rating = total_rating // total_cards

        else:
            avg_rating = 0

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
