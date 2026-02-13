#!/usr/bin/env python3

# We are going to check some errors result to make especific Exceptions.
# Due to the limitations in the authorized functions there are some
# errors than will be done with unauyhorized functions.

def garden_operations(error_type):

    if error_type == "value":
        int("abc")
    elif error_type == "zero":
        10 / 0
    elif error_type == "file":
        open("no-file")
    elif error_type == "key":
        {"x": 1}['missing_plant']


def test_error_types():

    # ValueError checks if the input given is possible with the given
    # variable type and/or values limits.

    try:
        garden_operations("value")
    except ValueError as e:
        print(f"Caught ValueError:{e}\n")

    # ZeroDivisionError, as his name shows, works for indetermination
    # of elements divided by 0.

    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError:{e}\n")

    # FileNotFouldError is the generic return when you try to acced to
    # a file not reacheable or existent. Because we have not an open
    # function authorized or any other

    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught FileNotFound:{e}\n")

    # KeyError is used when the dictionary can find an entry.

    try:
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError:{e}\n")

    # Here we try all the errors at one, checking taht it doesn't stops
    # the execution when it finds an error while using try and except.

    try:
        garden_operations("value")
        garden_operations("zero")
        garden_operations("file")
        garden_operations("key")
    except Exception:
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


if __name__ == "__main__":

    test_error_types()
