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


def main() -> None:
    print("=== Plant Factory Output ===")
    plants: list[Plant] = [
        Plant(name="rose", height=25, days=30, growth_rate=0.8),
        Plant(name="oak", height=200, days=365, growth_rate=0.1),
        Plant(name="cactus", height=5, days=90, growth_rate=0.2),
        Plant(name="sunflower", height=80, days=45, growth_rate=0.5),
        Plant(name="fern", height=15, days=120, growth_rate=0.3)
    ]
    for plant in plants:
        print("Created:", end=" ")
        plant.show()


if __name__ == "__main__":
    main()
