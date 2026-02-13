from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1 import SpellCard, ArtifactCard, Deck
from typing import Dict
import random


class FantasyCardFactory(CardFactory):

    """
    Class that inherit from Cardfactory and reinterpretate all his functions.
    It generates cards of each types based on the generic Card class from ex0

    Methods:
        - create_creature(): creates a creature card and adds it to the
        accesible list of cards.
        - create_spell(): creates a new spell and adds it to the accesible
        list of cards.
        - create_artifact(): creates a new artifact and adds it to the
        accesible list of cards.
        - get_supported_types(): returns a dictionary with all the suported
        cards with the basic types in the card list.
        - create_themed_deck(): Generates a new deck with all the cards with
        the "Creature" type.
    """

    def __init__(self):

        self.list_of_cards = [CreatureCard("Fire Dragon", 5, "Legendary",
                                           7, 10),
                              CreatureCard("Young Wolf", 1, "Common", 1, 1),
                              CreatureCard("Goblin Warrior", 3, "Uncommon",
                                           3, 1),
                              SpellCard("Lightning Bolt", 1, "commmon",
                                        "Deals 3 point to target minion"),
                              SpellCard("Nature's claim", 1, "common",
                                        "Destroy target artifact"),
                              ArtifactCard("Mana Crystal", 2, "rare", 3,
                                           "Add 1 mana to your manapool")]

    def create_creature(self, name: str, cost: int, rarity: str,
                        attack: int, health: int):
        card = CreatureCard(name, cost, rarity, attack, health)
        self.list_of_cards = self.list_of_cards + [card]
        return card

    def create_spell(self, name: str, cost: int, rarity: str, effect: str):
        card = SpellCard(name, cost, rarity, effect)
        self.list_of_cards = self.list_of_cards + [card]
        return card

    def create_artifact(self, name: str, cost: int, rarity: str,
                        durability: int, effect: str):
        card = ArtifactCard(name, cost, rarity, durability, effect)
        self.list_of_cards = self.list_of_cards + [card]
        return card

    def get_supported_types(self) -> Dict:
        output = {}
        for card in self.list_of_cards:
            card_type = card.type

            if card_type not in output:
                output[card_type] = []

            output[card_type] = output[card_type] + [card.name]

        return output

    def create_themed_deck(self, size: int) -> Deck:

        deck = Deck()
        main_cards = []
        i = 0

        for card in self.list_of_cards:
            if card.type == "Creature":
                main_cards = main_cards + [card]

        if main_cards == []:
            return deck

        while i < size:
            deck.add_card(random.choice(main_cards))
            i += 1

        deck.shuffle()
        return deck
