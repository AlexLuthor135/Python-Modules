#!/usr/bin/python3

import math


def get_player_pos() -> tuple[float, float, float]:
    position: list[str] = []
    numbers: list[float] = []
    completed: bool = False
    while not completed:
        try:
            while len(position) != 3:
                position = input(
                    "Enter new coordinates as floats in format 'x,y,z': "
                    ).split(',')
                if len(position) != 3:
                    print("Invalid syntax")
                    continue
            for p in position:
                numbers += [float(p)]
            completed = True
        except ValueError as e:
            position.clear()
            numbers.clear()
            print(f"Error on parameter '{p}': {e}")
    numbers_tuple: tuple[float, float, float] = (
        numbers[0], numbers[1], numbers[2]
        )
    return numbers_tuple


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    one: tuple[float, float, float] = get_player_pos()
    print(f'Got a first tuple: {one}')
    print(f'It includes: X={one[0]}, Y={one[1]}, Z={one[2]}')
    center: float = round(math.sqrt(one[0]**2 + one[1]**2 + one[2]**2), 4)
    print(f'Distance to center: {center}')
    print("\nGet a second set of coordinates")
    two: tuple[float, float, float] = get_player_pos()
    distance: float = round(math.sqrt(
        (two[0] - one[0])**2 + (two[1] - one[1])**2 + (two[2] - one[2])**2
        ), 4)
    print(f'Distance between the 2 sets of coordinates: {distance}')
