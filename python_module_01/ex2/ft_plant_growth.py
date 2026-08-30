#!/usr/bin/python3

class Plant:
    name: str
    height: float
    days: int
    growth_rate: float
    initial_height: float

    def __init__(self, name: str, height: float, days: int, growth_rate: float
                 ) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate
        self.initial_height = height

    def show(self) -> None:
        print(f'{self.name.capitalize()}:',
              f'{self.height:.1f}cm, {self.days} days old')

    def age(self) -> None:
        self.days += 1

    def grow(self) -> None:
        self.height += self.growth_rate


def weekly_result(plants: list[Plant]) -> None:
    print("=== Garden Plant Growth ===")
    day: int = 1
    for plant in plants:
        plant.show()
        plant.initial_height = plant.height
    while day <= 7:
        print(f"=== Day {day} ===")
        for plant in plants:
            plant.age()
            plant.grow()
            plant.show()
        day += 1
    for plant in plants:
        height_growth: float = round(plant.height - plant.initial_height, 2)
        print(f"Growth this week: {height_growth}cm")


def main() -> None:
    plants: list[Plant] = [
        Plant(name="rose", height=25, days=30, growth_rate=0.8)
    ]
    weekly_result(plants)


if __name__ == "__main__":
    main()
