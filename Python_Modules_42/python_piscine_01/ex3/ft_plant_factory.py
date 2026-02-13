#!/usr/bin/env python3

# This is the first proyect we need to create and display any number of
# objects. We can create and inizialize them in the "all_plants" array
# to have easy acces to them.


class Plant:

    # Having the array as a static element in the class give us the
    # oportunity to acces to his information from any of the element
    # who share the same class.

    all_plants = []

    def __init__(self, name, age, high, growth_rate, max_high):

        self.name = name
        self.age = age
        self.high = high
        self.growth_rate = growth_rate
        self.max_high = max_high
        Plant.all_plants = Plant.all_plants + [self]

    # As we are re-using the class, we still have some funtions to modify
    # some aspects of our class.

    def ageing(self):

        self.age += 1

    def growth(self):
        if self.age < 20 and self.high < self.max_high:

            self.high += self.growth_rate

        elif self.age >= 20 and self.high < self.max_high:

            self.high += self.growth_rate * 0.5

    # Here is our funtion to display all the plants in the "all_plants array"

    def get_info(self):

        i = 0
        print("===Plant Factory Output===")
        for plant in Plant.all_plants:
            print((f"Created: {plant.name} ({plant.high} cm, "
                   f"{plant.age} days)"))
            i += 1
        print(f"\nTotal plants created : {i}")

        return


"""if __name__ == "__main__":

    plant1 = Plant("Rose", 10, 3, 1.2, 60)
    plant2 = Plant("Sunflower", 17, 30, 2.5, 120)
    plant3 = Plant("Lilly", 2, 10, 0.5, 70)
    plant4 = Plant("Fern", 7, 1, 0.7, 22)
    plant5 = Plant("Oak", 70, 223, 12, 98)
    plant6 = Plant("Bacon", 777, 2230, 122, 984)

    plant1.get_info()"""
