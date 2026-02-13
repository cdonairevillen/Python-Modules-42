#!/usr/bin/env python3

# This function checks the input gived to make a comparative.
def ft_plant_age():

    age = int(input("Enter plant age in days:"))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
