try:
    from .basic import lead_to_gold, stone_to_gem
    from .advanced import philosophers_stone, elixir_of_life
except Exception:
    print("This must not be executed, dummy")

if __name__ == "__main__":

    try:
        print(lead_to_gold())
        print(stone_to_gem())
        print(philosophers_stone())
        print(elixir_of_life())
    except Exception:
        print("This must not be executed, dummy")
