#!/usr/bin/env python3

# This function recibe inputs to create a garden.
# If the number input is not a number, it displays an error.
# Then it displays the information.
def ft_garden_summary():

    name = input("Enter garden name:")
    plants = input("Enter number of plants:")

    for c in plants:
        if c < '0' or c > '9':
            print("Error:You need to set a number.")
            return
    print("Garden:", name)
    print("Plants:", plants)
    print("Status: Growing well!")
