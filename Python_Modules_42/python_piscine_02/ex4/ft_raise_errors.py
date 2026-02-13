#!/usr/bin/env python3

# As you can raise personalized errors, you can raise common errors too.

def check_plant_health(plant_name, water_level, sunlight_hours):

    if plant_name == "" or plant_name is None:
        raise ValueError
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif 1 > water_level:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if 2 > sunlight_hours:
        raise ValueError(f"Sunlight level {sunlight_hours} is too low (min 2)")
    elif 12 < sunlight_hours:
        raise ValueError(f"Sunlight level {sunlight_hours} "
                         f"is too high (max 12)")
    print(f"Plant '{plant_name}' is healthy")


# You can do the same as you personal errors with te structure of try/except.

def ft_raise_errors():

    try:
        print("Testing empty plant name...")
        check_plant_health("", 6, 3)
    except ValueError:
        print("Error: Plant name cannot be empty!")

    try:
        print("Testing bad water level...")
        check_plant_health("", 45, 3)
    except ValueError as f:
        print("Error:", f)

    try:
        print("Testing bad sunlight hours...")
        check_plant_health("", 4, 1)
    except ValueError as f:
        print("Error:", f)


if __name__ == "__main__":

    ft_raise_errors()
