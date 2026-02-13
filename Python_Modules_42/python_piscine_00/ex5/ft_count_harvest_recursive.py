#!/usr/bin/env python3

# Does a recursive iteration until the day to harvest
def ft_count_harvest_recursive(i=1, days=None):

    if days is None:
        days = int(input("Days until harvest:"))
    if i > days:
        print("Harvest time!")
        return
    print(f"Day: {i}")
    ft_count_harvest_recursive(i+1, days)
