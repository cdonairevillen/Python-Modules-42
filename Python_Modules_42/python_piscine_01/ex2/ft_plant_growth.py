#!/usr/bin/env python3

class Plant:

    def __init__(self, name, age, high, growth_rate, max_high):

        self.name = name
        self.age = age
        self.high = high
        self.growth_rate = growth_rate
        self.max_high = max_high

    # Functions can be used to change the information setted in __init__
    # Here we change the age and high from each plant created.

    def ageing(self):

        self.age += 1

    def growth(self):
        if self.age < 20 and self.high < self.max_high:

            self.high += self.growth_rate

        elif self.age >= 20 and self.high < self.max_high:

            self.high += self.growth_rate * 0.5

    # As in ex1, we have created a funtion to display the __init__
    # variable situation as the evolution of the variables in 'i' days

    def get_info(self, days):

        high = self.high
        i = 0
        print("===Garden Plant Registry===")
        print(f"===Day {i}===")
        print(f"{self.name}: {self.high:.2f} cm, {self.age} days old")
        while i < days:
            self.ageing()
            self.growth()
            i += 1

        print(f"===Day {i}===")
        print(f"{self.name}: {self.high:.2f} cm, {self.age} days old")
        print("____________")
        print(f"{self.high - high:.2f}")
        return


"""if __name__ == "__main__":

    plant1 = Plant("Rose", 10, 3, 1.2, 60)
    plant2 = Plant("Sunflower", 17, 30, 2.5, 120)
    plant3 = Plant("Lilly", 2, 10, 0.5, 70)
    days = 7

    plant1.get_info(days)
    plant2.get_info(days)
    plant3.get_info(days)"""
