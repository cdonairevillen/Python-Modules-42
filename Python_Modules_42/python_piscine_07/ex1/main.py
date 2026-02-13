#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck

if __name__ == "__main__":

    game_state = {"mana": 7}
    max_hand = 3

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

    print("=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")
    print("Deck stats:", my_deck.get_deck_status())
    print()
    print("Drawind and playing cards:\n")

    my_deck.shuffle()
    i = 0
    while i < max_hand:
        my_hand = my_hand + [my_deck.draw_card()]
        print(f"Drew: {my_hand[i].name} ({my_hand[i].type})")
        print("Play result:", my_hand[i].play(game_state))
        print()
        i += 1

    print("Polymorphism in action: Same interface, different card behaviors!")
