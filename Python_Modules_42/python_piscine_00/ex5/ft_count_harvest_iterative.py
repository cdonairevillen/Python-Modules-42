#!/usr/bin/env python3

# Does a iterative iteration until the day to harvest
def ft_count_harvest_iterative():

    days = int(input("Days until harvest:"))
    i = 1
    while i in range(1, days + 1):
        print(f"Day: {i}")
        i += 1
    print("Harvest time!")
