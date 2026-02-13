#!/usr/bin/env python3
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

if __name__ == "__main__":

    platform = TournamentPlatform()

    dragon = TournamentCard("Shyvan Dragon", 5, "rare", 5, 5)
    wizard = TournamentCard("Snapcaster Mage", 2, "rare", 2, 1)

    print("=== Data Deck Tournament Platform ===")
    print()
    print("Registering Tournament Cards...")
    print()
    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    for card_id, card in platform.cards.items():
        print(f"{card.name} (ID: {card_id})")
        print(f"- Interfaces: {platform.interfaces}")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins} - {card.losses}")
        print()

    print("Creating tournament match...")
    result = platform.create_match(dragon_id, wizard_id)
    print("Match result:", result)
    print()
    print("Tournament Laderboard:")
    laderboard = platform.get_leaderboard()

    pos = 1
    for card in laderboard:
        print(f"{pos}. {card['name']} - Rating: {card['rating']}"
              f" ({card['wins']} - {card['losses']})")
    print()
    print("Platform Report:")
    report = platform.generate_tournament_report()
    print(report)
    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
