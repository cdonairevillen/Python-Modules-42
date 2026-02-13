#!/usr/bin/env python3

# Here are some personalized errors made for myself. They all inherit from
# exception.

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class SunlightError(GardenError):
    pass

# Here we have a class Plant that will have some general information about
# our object.


class Plant():

    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun

# GardenManager will make all the checks needed to make our garden thrive.
# We will be using the construction try/except in each of our functions.


class GardenManager():
    def __init__(self):

        self.plants = []
        self.tank = 5

    # This function try to add a valid plant to the plants array
    def add_plant(self, plant):

        try:
            if plant.name == "" or plant.name is None:
                raise PlantError("Plant name cannot be empty!")
            self.plants = self.plants + [plant]
            print(f"Added {plant.name} successfully!")
        except PlantError as c:
            print("Error :", c)

    # This function ties to Water all the plants in the list.

    def water_plants(self, water_level):

        print("\nOpening watering system\n")
        try:
            for plant in self.plants:
                if self.tank > 0:
                    plant.water += water_level
                    self.tank -= water_level
                    print(f"Watering {plant.name} -- Success")
                else:
                    raise WaterError("Not enough water to water the plants")
        except WaterError as c:
            print("Error:", c)
        finally:
            print("\nClosing Watering System (cleanup)\n")

    # This function checks if the light levels are correct.

    def check_plants_health(self, plant):
        if plant.name == "" or plant.name is None:
            raise PlantError("Plant name cannot be empty")
        if plant.water > 10:
            raise WaterError(f"{plant.name} Water level {plant.water} is too "
                             "high")
        if plant.water < 1:
            raise WaterError(f"{plant.name} Water level {plant.water} is too "
                             "low")
        if plant.sun < 2:
            raise SunlightError(f"{plant.name} Sun level {plant.sun} is too "
                                "low")
        if plant.sun > 12:
            raise SunlightError(f"{plant.name} Sun level {plant.sun} is "
                                "too high")
        else:
            print(f"{plant.name} is healty! (water :{plant.water}, sun : "
                  F"{plant.sun})")

    # This function checks the water level of the manager.

    def testing_error_recovering(self, water):
        for plant in self.plants:
            self.tank -= water
        if self.tank > 0:
            print("There are still water in the tank")
        else:
            raise GardenError("Not enough water in tank")

    # This function calls all the tests from GardenManager.
    def test_manager(self, water):
        self.water_plants(water)
        for plant in self.plants:
            try:
                self.check_plants_health(plant)
            except GardenError as c:
                print("Error:", c)
        try:
            print("\nTesting Error Recovery\n")
            self.testing_error_recovering(water)
        except GardenError as c:
            print("Caught GardenError:", c)
            print("System recovered and continuing...\n")
        finally:
            print("Garden management system test complete!")


if __name__ == "__main__":

    plant1 = Plant("Tomato", 3, 5)
    plant2 = Plant("Letuce", 1, 15)
    plant3 = Plant("Bacon", 5, 5)
    plant4 = Plant("", 5, 23)
    garden1 = GardenManager()

    garden1.add_plant(plant1)
    garden1.add_plant(plant2)
    garden1.add_plant(plant3)
    garden1.add_plant(plant4)
    garden1.test_manager(3)
