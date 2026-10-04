#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def plant_error(message: str) -> None:
    raise PlantError(message)


def water_error(message: str) -> None:
    raise WaterError(message)


def raise_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        plant_error("The tomato plant is wilting!")
    except PlantError as e:
        print(f'Caught PlantError: {e}')
    print("\nTesting WaterError...")
    try:
        water_error("Not enough water in the tank!")
    except WaterError as e:
        print(f'Caught WaterError: {e}')
    print("\nTesting catching all garden errors...")
    try:
        plant_error("The tomato plant is wilting!")
    except GardenError as e:
        print(f'Caught GardenError: {e}')
    try:
        water_error("Not enough water in the tank!")
    except GardenError as e:
        print(f'Caught GardenError: {e}')
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    raise_errors()
