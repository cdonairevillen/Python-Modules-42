#!/usr/bin/env python3

import sys


def ft_argv_control():

    """
    Exercise to lear about how to introduce arguments from console in python.

    Variables:
        - sys.argv: array with all the information provided by console
        sys.argv[0] always contain the program name.

    Functionality:
        - Prints all the information from the arguments provided

    Returns:
        - This function doesnt returns anything.
    """

    print("=== Comand Quest ===")

    if len(sys.argv) == 1:
        print("No arguments provided")
        print("Program name:", sys.argv[0])
    else:
        print("Program name:", sys.argv[0])
        print("Arguments recived:", len(sys.argv) - 1)
        i = 1
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print("Total arguments:", len(sys.argv))


if __name__ == "__main__":
    ft_argv_control()
