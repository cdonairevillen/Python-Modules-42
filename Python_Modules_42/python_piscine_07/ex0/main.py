from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":

    game_state = {
            "mana": 6
    }

    available_cards = [CreatureCard("Fire Dragon", 5, "Legendary", 7, 10),
                       CreatureCard("Young Wolf", 1, "Common", 1, 1),
                       CreatureCard("Goblin Warrior", 3, "Uncommon", 3, 1)]

    enemy_card = CreatureCard("Goblin Warrior", 3, "Uncommon", 3, 1)

    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()
    print("CreatureCard Info:")
    print(available_cards[0].get_card_info())
    print()
    print(f"Playing {available_cards[0].name} with {game_state['mana']} mana"
          " available:")
    print(f"Playable: {available_cards[0].is_playable(game_state['mana'])}")
    print("Play result:", available_cards[0].play(game_state))
    print()
    print(f"{available_cards[0].name} attacks {enemy_card.name}")
    print("Attack result:", available_cards[0].attack_target(enemy_card))
    print()
    print(f"Testing insufficient mana ({game_state['mana']} available)")
    print("Playable:", available_cards[2].is_playable(game_state['mana']))
    print()
    print("Abstract pattern successfully demonstrated!")
