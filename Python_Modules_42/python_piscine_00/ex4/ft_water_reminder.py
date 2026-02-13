#!/usr/bin/env python3

# This function checks the input to make a comparative
def ft_water_reminder():

    if int(input("Days since last watering:")) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
