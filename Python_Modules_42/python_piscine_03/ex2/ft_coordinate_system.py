#!/usr/bin/env python3

import sys
import math


def ft_len(obj):

    """
    Recreation of len() function because is not autorized.
    """
    count = 0
    for element in obj:
        count += 1
    return count


def ft_coordinate_system(*args):

    """
    Generates a coordinate system taking the entries from arguments
    and/or direct entry.

    Variables:
        - args: all the arguments provided to the program
        - zero: tuple setted with origin coordinates.
        - pos: accesible splited int parameters encapsulated in a tuple
                after checking the entry.
        - dis: result of the euclidean distance from zero to pos

    Functionality:
        - The function checks the entry parameters. If there is none,
        it uses the sys.argv excluding the one in the position 0
        - If the entry checked is just 1, it splits the argument
        in each comma and tries to fill the pos tuple with int.
        - If the entry checked is 3, it tries to fill the position
        tuple directly.
        - Once parsed the entry, it makes the math calculation.
        -if anything goes wrong, it prints the value error msg.

    Returns:
        - This function doesnt returns anything.
    """

    zero = tuple([0, 0, 0])

    if ft_len(args) == 0:
        args = sys.argv[1:]

    try:
        if ft_len(args) == 1:
            part = args[0].split(",")
            if ft_len(part) == 3:
                pos = (int(part[0]), int(part[1]), int(part[2]))
            else:
                print("Invalid number of arguments")
                return
            print("Parsed position:", pos)

        elif ft_len(args) == 3:
            pos = (int(args[0]), int(args[1]), int(args[2]))

        else:
            print("Invalid number of arguments")
            return

        dis = math.sqrt((pos[0]-zero[0])**2 + (pos[1]-zero[1])**2
                        + (pos[2]-zero[2]**2))

        print(f"Distance between {zero} and {pos}: {dis:.2f}")

    except ValueError as e:
        print("Error parsing coordinates:", e)
        print("Error details - Type: ValueError, Args", e.args)
    print("\n")


if __name__ == "__main__":

    print("=== Game Coordinate System ===\n")
    print("Position created: (10, 20, 5)")
    ft_coordinate_system(10, 20, 5)
    print("Parsing coodinates: \"3,4,0\"")
    ft_coordinate_system("3,4,0")
    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    ft_coordinate_system("abc,def,ghi")
    print(f"Imput position: {sys.argv[1:]}")
    ft_coordinate_system()
