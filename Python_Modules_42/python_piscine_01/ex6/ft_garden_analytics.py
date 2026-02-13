#!/usr/bin/env python3

# Here we havo some class created to set some objects to each garden.
class Plant:

    type_name = "regular"

    def __init__(self, name, age, hight):
        self.name = name
        self._age = age
        self.initial_hight = hight
        self._hight = hight

    # As in the last ex, I'll get the info of each element just returning them
    # to the general printer.

    def get_info(self):
        return (f"{self.name}: {self._hight}cm, {self._age} days")

# This function inherit from "Plant" the values for "name", "age" and "hight"


class FloweringPlant(Plant):

    # As with the array from Managers, we can set generic information that are
    # that is sheared with all objects who share the class
    type_name = "flowering"

    def __init__(self, name, age, hight, color, bloom):
        super().__init__(name, age, hight)
        self.color = color
        self.bloom = bloom

    # We check if the bloom flag is on to all the information to the get_info

    def blooming(self):
        if self.bloom is True:
            return ("(blooming)")
        else:
            return ("(not bloomed)")

    # As in the last ex, I'll get the info of each element just returning them
    # to the general printer.

    def get_info(self):
        base = super().get_info()
        return (f"{base}, color: {self.color} {self.blooming()}")

# This class inherit from "Flowering plant" and adds a award acont to ifself
# just to increase in 1 the counter when the function is called.


class PrizeFlower(FloweringPlant):

    type_name = "prize"

    def __init__(self, name, age, hight, color, bloom, aw_count):
        super().__init__(name, age, hight, color, bloom)
        self.aw_count = aw_count

    # This function increases in 1 the count in aw_count and returns the
    # the output to the printer if the function is called.

    def enter_competition(self):
        self.aw_count += 1
        return (f"{self.name} entered competition an now has {self.aw_count}")

# GardenManager is a class that controls and separates the gardens from
# diferent gardeners. Using the "all_managers" array we can acces to the garden
# of any person setted in it.


class GardenManager():

    all_managers = []

    def __init__(self, owner_name):
        self.owner = owner_name
        self.score = 0
        GardenManager.all_managers = GardenManager.all_managers + [self]
        self.plants = []

    # As a Manager we can add plants to the garden we want.

    def add_plant(self, plant):
        self.plants = self.plants + [plant]
        print(f"Added {plant.name} to {self.owner}'s garden")

    # We can access to the information of any plant in the garden we are
    # manageing

    def list_plants(self):
        print("Plants in garden")
        for p in self.plants:
            print("-", p.get_info())

    # This function allow to grow our plants in the garden we are manageing

    def grow(self):
        for plant in self.plants:
            plant._hight += 1
            print(f" - {plant.name} grew 1cm.")

    # @classmethod are functions that works in a class. They recieve the whole
    # class and can check all objects there are created.
    # We can use them to set scores to all the gardens in just one call.

    @classmethod
    def set_score(cls):
        for manager in cls.all_managers:
            for plant in manager.plants:
                if plant.type_name == "regular":
                    manager.score += 10
                elif plant.type_name == "flowering":
                    manager.score += 25
                elif plant.type_name == "prize":
                    manager.score += 50

    # See how many gardens are actives checking the number of managers created

    @classmethod
    def total_gardens(cls):
        i = 0
        for managers in cls.all_managers:
            i += 1
        print(f"Total gardens managed: {i}")

    # @staticmethod is ust a normal function kept in a class. It doesn't need
    # information from the class to work (doesn't acces to self or cls)
    # just a way to organize the project

    @staticmethod
    def validate_hight(hight):
        if hight >= 0:
            print("hight validation test: TRUE")
        else:
            print("hight validation test: FALSE")

    # Usually python doesn't needs to create dependences in clases, makeing
    # them being inside one to other. It can serve some purposes like
    # encapsulate information and indicate dependence, but is not really
    # necesary.

    class GardenStats():
        def __init__(self, plants):
            self.plants = plants

        # This function count the amount of plants in each garden.

        def total_plants(self, owner):
            i = 0
            for plant in self.plants:
                i += 1
            print(f"Plants added: {i} in {owner}'s garden")

        # This function count the amount of plant of each type in each
        # garden

        def count_type(self):
            reg = 0
            fl = 0
            pr = 0
            for plant in self.plants:
                if plant.type_name == "regular":
                    reg += 1
                elif plant.type_name == "flowering":
                    fl += 1
                elif plant.type_name == "prize":
                    pr += 1
            print(f"There are: {reg} regular, {fl} flowering and {pr} prized")

        # This function regist te total growth the garden has had in this
        # iteration.

        def total_growth(self):
            total = 0
            for p in self.plants:
                total += (p._hight - p.initial_hight)
            print(f"Total growth: {total}cm")

# This is a builder made just to make the output be the same as the shown in
# the subject. Here we set Managers for each garden and we can acces to the
# information kept in each of them.


def ft_garden_analitics():

    print("=== Garden Management System Demo ===\n")

    garden1 = GardenManager("Alice")
    garden2 = GardenManager("Bob")

    plant1 = FloweringPlant("Rose", 10, 20, "red", True)
    plant2 = Plant("Oak", 50, 100)
    plant3 = PrizeFlower("Bacon", 10, 20, "creamy", False, 50)

    garden1.add_plant(plant3)
    garden1.add_plant(plant2)
    garden1.add_plant(plant1)
    garden1.add_plant(plant1)

    print("\n")

    garden2.add_plant(plant2)
    garden2.add_plant(plant2)
    garden2.add_plant(plant1)

    print("\nAlice is helping all plants grow...")
    garden1.grow()

    print("\n=== Alice's Garden Report ===")
    stats = garden1.GardenStats(garden1.plants)
    for plant in garden1.plants:
        if plant.type_name == "regular":
            print(f" - {plant.name}: {plant._hight}")
        elif plant.type_name == "flowering":
            print(f" - {plant.name}: {plant._hight}, {plant.color}, "
                  f"{plant.blooming()}")
        elif plant.type_name == "prize":
            print(f" - {plant.name}: {plant._hight}, {plant.color}, "
                  f"{plant.blooming()}, Prize points: {plant.aw_count}")
    print("\n")

    stats.total_plants("Alice")
    stats.total_growth()
    stats.count_type()
    print("\n")

    GardenManager.validate_hight(plant1._hight)
    GardenManager.validate_hight(-5)
    GardenManager.set_score()
    print(f"Garden scores - Alice: {garden1.score}, Bob: {garden2.score}")
    GardenManager.total_gardens()


"""if __name__ == "__main__":

    ft_garden_analitics()"""
