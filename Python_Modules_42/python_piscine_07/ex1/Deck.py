#!/usr/bin/env python3

import random
from typing import Dict
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck():

    """
    Class that creates a new Deck where will be compiled all the created cards.

    Methods:
        - add_card(): adds a new card to the full_deck array
        - play(): removes 1 named card from the full_deck array
        - shuffle(): uses the random library to shuffle the full_deck array.
        - draw_card(): draws and returns the card drown to the main program.
        It deletes the first position from the full_deck array.
    """

    full_deck = []

    def add_card(self, card: Card) -> None:
        self.full_deck = self.full_deck + [card]

    def remove_card(self, card_name: str) -> bool:
        new_deck = []
        removed = False
        for card in self.full_deck:
            if card_name == card.name and not removed:
                removed = True
            else:
                new_deck = new_deck + [card]

        self.full_deck = new_deck
        return removed

    def shuffle(self) -> None:
        random.shuffle(self.full_deck)

    def draw_card(self) -> Card:
        len = 0
        for card in self.full_deck:
            len += 1

        if len == 0:
            return None
        drawn = self.full_deck[0]
        self.full_deck = self.full_deck[1:]
        return drawn

    def get_deck_status(self) -> Dict:
        status = {
            "total_cards": 0,
            "Creature": 0,
            "Artifact": 0,
            "Spell": 0
        }
        for card in self.full_deck:
            status["total_cards"] += 1
            if card.type in status:
                status[card.type] += 1

        return status


if __name__ == "__main__":

    my_deck = Deck()

    my_hand = []

    list_of_cards = [CreatureCard("Fire Dragon", 5, "Legendary", 7, 10),
                     CreatureCard("Young Wolf", 1, "Common", 1, 1),
                     CreatureCard("Goblin Warrior", 3, "Uncommon", 3, 1),
                     SpellCard("Lightning Bolt", 1, "commmon",
                               "Deals 3 point to target minion"),
                     SpellCard("Nature's claim", 1, "common",
                               "Destroy target artifact"),
                     ArtifactCard("Mana Crystal", 2, "rare", 3,
                                  "Add 1 mana to your manapool")]

    for card in list_of_cards:
        my_deck.add_card(card)

    print(my_deck.get_deck_status())
    print("-----------------------------------------")
    my_deck.shuffle()
    card_drawn = my_deck.draw_card()
    my_hand = my_hand + [card_drawn]

    for card in my_hand:
        print(card.get_card_info())

    print(my_deck.get_deck_status())

    print("-----------------------------------------")
