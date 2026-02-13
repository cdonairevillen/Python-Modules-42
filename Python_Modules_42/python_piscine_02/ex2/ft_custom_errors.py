#!/usr/bin/env python3

# We can create our own errors makeing inherit from the generic problem
# "Exception". It takes the prints and creates the message the same way
# as the "Exception" does.

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class Watererror(GardenError):

    pass

# "raise" is a action that allows us to force an error in a try/except check.


def test_plant_error():
    raise PlantError("Tomato plant is wilting!")


def test_water_error():
    raise Watererror("Not enough water in the tank")

# This function checks all the personalized errors we have defined


def test_error_types():

    try:
        print("Testing plant errors:\n")
        test_plant_error()
    except PlantError as e:
        print(f"Caught PlantError:{e}\n")

    try:
        print("Testing water errors:\n")
        test_water_error()
    except Watererror as f:
        print(f"Caught PlantError:{f}\n")

    print("Testing all errors:\n")

    try:
        test_plant_error()
    except GardenError as g:
        print(f"Caught a garden error:{g}")

    try:
        test_water_error()
    except GardenError as g:
        print(f"Caught a garden error:{g}\n")


if __name__ == "__main__":

    test_error_types()
