#!/usr/bin/env python3

# This function gives you the area of a square surface (length * widht)
def ft_plot_area():
    length = input("Enter length: ")
    width = input("Enter width: ")

    length = int(length)
    width = int(width)

    area = length * width

    print("Plot area: ", area)
