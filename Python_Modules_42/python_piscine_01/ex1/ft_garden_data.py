#!/usr/bin/env python3

# Classes are information containers, close to structures in 'C'.
# You can set some common information accesible only by the object
# like "all_plants" array, and set personalized information
# for any object that has the class using __init__


class Plant:

    all_plants = []

    def __init__(self, name, age, high):

        self.name = name
        self.age = age
        self.high = high
        Plant.all_plants = Plant.all_plants + [self]

    # As an object, they can have specific functions. This one
    # prints the information setted in as the objject is created.
    def get_info(self):

        print("===Garden Plant Registry===")
        for element in Plant.all_plants:
            print(f"{element.name} : {element.age} days, {element.high} cm")
        return


"""if __name__ == "__main__":

    plant1 = Plant("Rose", 10, 3)
    plant2 = Plant("Sunflower", 17, 30)
    plant3 = Plant("Lilly", 2, 10)

    plant1.get_info()"""
