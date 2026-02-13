#!/usr/bin/env python3

# Classes can inherit informations from one to other.
# Here we have a generic plant setter who is the parent of a hereditary line.
# We set generic parameters that can be shared by their heirs.

class Plant:

    all_plants = []

    def __init__(self, name, age, height):

        self.name = name
        self._age = age
        self._height = height

# This class inherit from Plant. We use the "super()." funtion to get the
# information provided in the parent class and add them to the builder.


class Flower(Plant):
    def __init__(self, name, age, height, color, bloomed):
        super().__init__(name, age, height)
        self.color = color
        self.bloomed = bloomed
        self.type = "flower"
        Plant.all_plants = Plant.all_plants + [self]

    # Due how have I face this ex, this functions retuns the information from
    # each objet to a generic printer function.

    def get_info(self):
        return (f"{self.name} (Flower): {self._height}cm, "
                f"{self._age} days, {self.color} color")

    def set_bloomed(self):
        if self.bloomed > 0:
            return (f"{self.name} is blooming beautifully!")
        else:
            return (f"{self.name} still hasn't bloomed")

# As the preview class, this class inherit from pant and adds another elements
# to set as his own.


class Tree(Plant):
    def __init__(self, name, age, height, diam, shadow):
        super().__init__(name, age, height)
        self.diam = diam
        self.shadow = shadow
        self.type = "tree"
        Plant.all_plants = Plant.all_plants + [self]

    # Due how have I face this ex, this functions retuns the information from
    # each objet to a generic printer function.

    def get_info(self):
        return (f"{self.name} (Tree): {self._height}cm, "
                f"{self._age} days, {self.diam}cm diameter")

    def set_shadow(self):
        if self.shadow > 0:
            return (f"{self.name} provides {self.shadow} "
                    f"square meters of shade")
        else:
            return (f"{self.name} does not provide shadow")

# This class generates the variant "Vegetable", inherit fom plant "name", "age"
# and height


class Vegetable(Plant):
    def __init__(self, name, age, height, harvest, nutritive):
        super().__init__(name, age, height)
        self.harvest = harvest
        self.nutritive = nutritive
        self.type = "veg"
        Plant.all_plants = Plant.all_plants + [self]

    # Due how have I face this ex, this functions retuns the information from
    # each objet to a generic printer function.

    def get_info(self):
        return (f"{self.name} (Vegetable): {self._height}cm, {self._age} days,"
                f" {self.harvest} harvest")

    def set_nutritive(self):
        if self.nutritive > 0:
            return (f"{self.name} is rich in vitamin C")
        else:
            return (f"{self.name} is not really nutritive")

# This function displays the information of all plants created. The message
# printed is dependente of the subclass they are builded in.


def ft_plant_types():

    print("=== Garden Plant Types ===\n")
    for plant in Plant.all_plants:
        print(f"{plant.get_info()}")
        if plant.type == "flower":
            print(f"{plant.set_bloomed()}\n")
        elif plant.type == "tree":
            print(f"{plant.set_shadow()}\n")
        elif plant.type == "veg":
            print(f"{plant.set_nutritive()}\n")
        else:
            print("No info decided\n")


"""if __name__ == "__main__":

    plant1 = Flower("Rose", 10, 300, "red", -4)
    plant2 = Tree("Oak", 1450, 300, 86, 70)
    plant3 = Vegetable("Tomato", 33, 120, "summer", 0)

    ft_plant_types()"""
