#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex2.EliteCard import EliteCard


if __name__ == "__main__":

    game_state = {"mana": 3}
    max_hand = 3

    my_hand = []

    list_of_cards = [CreatureCard("Fire Dragon", 5, "Legendary", 7, 10),
                     CreatureCard("Young Wolf", 1, "Common", 1, 1),
                     CreatureCard("Goblin Warrior", 3, "Uncommon", 3, 1),
                     SpellCard("Lightning Bolt", 1, "commmon",
                               "Deals 3 point to target minion"),
                     SpellCard("Nature's claim", 1, "common",
                               "Destroy target artifact"),
                     ArtifactCard("Mana Crystal", 2, "rare", 3,
                                  "Add 1 mana to your manapool"),
                     EliteCard("Yawgmoth", 5, "Legendary", 3, 5, 2)]

    elitecard = list_of_cards[6]
    enemies = list_of_cards[:2]

    print("=== DataDeck Ability System ===")
    print("EliteCard capabilities:")
    print()
    print("- Card:", [EliteCard.attack.__name__,
                      EliteCard.get_card_info.__name__,
                      EliteCard.is_playable.__name__])
    print("- Combatable:", [EliteCard.attack.__name__,
                            EliteCard.defend.__name__,
                            EliteCard.get_combat_stats.__name__])
    print("- Magical:", [EliteCard.cast_spell.__name__,
                         EliteCard.channel_mana.__name__,
                         EliteCard.get_magic_stats.__name__])
    print()
    print(f"Playing {elitecard.name}, ({elitecard.type})")
    print()
    print("Combat phase:")
    print("Atack result:", elitecard.attack(enemies[1]))
    print("Defense result:", elitecard.defend(3))
    print()
    print("Combat phase:")
    print("Spell Cast:", elitecard.cast_spell("Defile", enemies[2:]))
    print("Mana Channel:", elitecard.channel_mana(2))
    print()
    print("Multiple interface implementation successful!")
