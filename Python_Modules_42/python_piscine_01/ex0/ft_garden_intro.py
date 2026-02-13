#!/usr/bin/env python3

# This is a generic function to show how the if __name__ == "__main__"
# works. Just print some generic information.

def ft_garden_intro():

    print("=====Garden Info:=====")

    print("Name: Rose")
    print("Height: 25cm")
    print("Age: 30 days")

    print("=====End of Program=====")

# This is a way to make a "realtive" main who will be exclude when this
# function would be called from any other progam.


if __name__ == "__main__":

    ft_garden_intro()
