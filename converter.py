from enum import Enum

BASE_DISTANCE_MAP = {
    "m": 1,
    "cm": 100,
    "mm": 1000,
    "km": 0.001,
    "in": 39.3701,
    "ft": 3.280841666667,
    "yd": 1.0936138888889999077,
    "mi": 0.000621371,
}
BASE_WEIGHT_MAP = {
    "L": 1,
    "mL": 1000,
    "floz": 33.814,
    "cup": 4.22675,
    "pint": 2.11338,
    "qt": 1.05669,
    "gal": 0.264172,
}
BASE_VOLUME_MAP = {"g": 1, "kg": 0.001, "mg": 1000, "oz": 0.035274, "lb": 0.00220462}
BASE_MAP = {**BASE_DISTANCE_MAP, **BASE_WEIGHT_MAP, **BASE_VOLUME_MAP}
DISTANCES = tuple(BASE_DISTANCE_MAP)
WEIGHTS = tuple(BASE_WEIGHT_MAP)
VOLUMES = tuple(BASE_VOLUME_MAP)
UNITS = set(DISTANCES + WEIGHTS + VOLUMES)


class Unit(Enum):
    DISTANCE = 1
    VOLUME = 2
    WEIGHT = 3


CATEGORIES = {
    **{d: Unit.DISTANCE for d in DISTANCES},
    **{v: Unit.VOLUME for v in VOLUMES},
    **{w: Unit.WEIGHT for w in WEIGHTS},
}


def print_banner():
    """
    Print the program banner. You may change the banner message.
    """
    print(
        """
Welcome to our Python-powered Unit Converter v1.0 by Adi Zimmerman!
You can convert Distances, Weights, Volumes to one another, but only
within units of the same category, which are shown below. E.g.: 1 mi in ft

   Distances: ft cm mm mi m yd km in
   Weights: lb mg kg oz g
   Volumes: floz qt cup mL L gal pint
"""
    )


def validate(command):
    args = command.split()
    if len(args) != 4:
        return "Error: Invalid format."
    amount, source_unit, connector, dest_unit = args
    if not isfloat(amount):
        return f"Error: Invalid AMOUNT:{amount}. Please enter a decimal"
    if source_unit not in UNITS:
        return f"Error: Invalid SOURCE_UNIT:{source_unit}. Valid units:{UNITS}"
    if dest_unit not in UNITS:
        return f"Error: Invalid DESTINATION_UNIT:{dest_unit}. Valid units:{UNITS}"
    if connector != "in":
        return f"Error: Invalid connector:{connector}. Please use 'in'"
    if CATEGORIES[source_unit] is not CATEGORIES[dest_unit]:
        return f"Error: Invalid categories. Tried to convert {CATEGORIES[source_unit]} {source_unit} to {CATEGORIES[dest_unit]} {dest_unit}"


def isfloat(amt):
    try:
        float(amt)
        return True
    except ValueError:
        return False


def convert(command):
    """
    Handle a SINGLE user input, which given the command, either print
    the conversion result, or print an error, or exit the program.
    Please follow the requirements listed on project website.
    :param command: User input

    >>> convert("1 m in km")
    1 m = 0.001000 km
    """
    if command == "q":
        quit()

    err = validate(command)
    if err:
        print(err)
        return

    amount, source_unit, connector, dest_unit = command.split()
    dest_amount = "{0:.6f}".format(
        float(amount) / BASE_MAP[source_unit] * BASE_MAP[dest_unit]
    )
    print(f"{amount} {source_unit} = {dest_amount} {dest_unit}")


def get_user_input():
    """
    Print the prompt and wait for user input
    :return: User input
    """
    return input("Convert [AMOUNT SOURCE_UNIT in DESTINATION_UNIT, or (q)uit]: ")


if __name__ == "__main__":
    print_banner()
    while True:
        command = get_user_input()
        convert(command)
