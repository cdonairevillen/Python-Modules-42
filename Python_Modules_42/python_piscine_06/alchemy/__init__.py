__version__ = "1.0.0"
__author__ = "Master Pythonicus"
try:
    from .elements import create_fire, create_water

except Exception:
    print("This must not be executed, dummy")

if __name__ == "__main__":
    try:
        print(create_fire())
        print(create_water())
    except Exception:
        print("This must not be executed, dummy")
