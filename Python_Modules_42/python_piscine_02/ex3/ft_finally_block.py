#!/usr/bin/env python3

# This function is the generic watering fnction that will be called by the
# tester. You can print the error rised as a variable extracted from exception.
# Last, we use finally to force the end in the try exectution. It allways will
# end in the finally.

def watering_plants(plant_list):

    print("Opening Watering System:")

    try:
        for plant in plant_list:
            if type(plant) is not str:
                raise Exception(f"Cannot water '{plant}' - invalid plant!")
            else:
                print(f"Watering {plant}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")

# This function is the tester. If it finds an error will recive the exception
# and print the generic error mesage.


def testing_watering_system():

    print("Testing normal watering\n")
    try:
        watering_plants(["a", "b", "c"])
        print("Watering completed successfully!\n")
    except Exception:
        print("Unexpected error!\n")

    print("Testing with error ...\n")
    try:
        watering_plants(["a", 23, "c"])
        print("This message should not appear!\n")
    except Exception:
        print("Cleanup always happens, even with an error!\n")


if __name__ == "__main__":

    testing_watering_system()
