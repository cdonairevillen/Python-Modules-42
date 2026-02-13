from ex3.AggresiveStrategy import AgresiveStrategy
from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory

if __name__ == "__main__":

    factory = FantasyCardFactory()
    strategy = AgresiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print("=== DataDeck Game Engine ===")
    print()
    print("Configuring Fantasy Card Game...")
    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())
    print()
    print("Simulating aggressive turn...")
    print(strategy.get_strategy_name())
    engine.configure_engine(factory, strategy)
    result = engine.simulate_turn()
    print("Actions:", result)
    print()
    print("Game Report:")
    print(engine.get_engine_status())
    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
