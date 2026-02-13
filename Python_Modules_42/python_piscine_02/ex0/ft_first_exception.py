#!/usr/bin/env python3

# In this piscine, we are we going to be working with error management.

def check_temperature(temp_str="10"):

    print(f"Testing temperature: {temp_str}")

    # We will use try to check if there are any error in the data we are
    # sending.

    try:
        temp = int(temp_str)
        if 0 <= temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!\n")
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (min 40°C)\n")
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number\n")

# This function just match the output with the showed in the subject


def test_temperature_input():

    print("=== Garden Temperature Checker ===\n")

    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")

    print("All tests completed - program didn't crash!\n")


if __name__ == "__main__":

    test_temperature_input()
