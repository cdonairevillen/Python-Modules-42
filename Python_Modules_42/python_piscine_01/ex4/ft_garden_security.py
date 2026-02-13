#!/usr/bin/env python3

# In this class we start working with restricted information. We can
# encapsulate information and check if set them as a valid imput
# with some special funtions.

class SecurePlant:

    def __init__(self, name, age, height):

        self.name = name
        self._age = age
        self._height = height

    # Property allows to acces to secure variables directly. We can set
    # the information just writing "pl1.age = x" or "self.age = x" if
    # we are seting it from the same class.

    @property
    def height(self):
        return self._height

    # Setters are automatic funtions that runs as the time you set the
    # information through a @property. They can be anything you want
    # but usually are just input checkers.
    # This function checks that the values of high are positive numbers.

    @height.setter
    def height(self, val):

        if val < 0:
            print(f"\nInvalid operation attempted: height {val}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        elif val != self._height:
            self._height = val
            print(f"Height updated: {self.height}cm [OK]")

    # Here we do de same just checking if the age of the plants is  valid
    # number.

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):

        if val < 0:
            print(f"\nInvalid operation attempted: age {val} days [REJECTED]")
            print("Security: Negative age rejected\n")
        elif val != self._age:
            self._age = val
            print(f"Age updated: {self.age} days [OK]")

    # This function print the info and try to make the changs in age and height
    # to display the information as the subject shows.
    def get_info(self):
        print("=== Garden Security System ===")
        print(f"Plant created: {self.name}")
        self.age = 100
        self.height = -3
        print(f"Current plant: {self.name} ({self.height}cm, {self.age} days)")


"""if __name__ == "__main__":

    pl1 = SecurePlant("Rose", 10, 3)

    pl1.get_info()"""
