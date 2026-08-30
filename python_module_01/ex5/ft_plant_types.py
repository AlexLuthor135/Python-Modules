#!/usr/bin/python3

class Plant:
    _name: str
    _height: float
    _days: int
    _growth_rate: float

    def __init__(self, name: str, height: float, days: int, growth_rate: float
                 ) -> None:
        self._name = name
        self._days = 0
        self._height = 0
        self._growth_rate = growth_rate
        self.set_age(days)
        self.set_height(height)

    def show(self) -> None:
        print(f'{self._name.capitalize()}:',
              f'{self._height:.1f}cm, {self._days} days old')

    def age(self) -> None:
        self._days += 1

    def grow(self) -> None:
        self._height += self._growth_rate

    def set_age(self, days: int) -> None:
        if days < 0:
            print(f"{self._name.capitalize()}:",
                  "Error, age can't be negative")
            return
        self._days = days

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name.capitalize()}:",
                  "Error, height can't be negative")
            return
        self._height = height

    def get_age(self) -> int:
        return self._days

    def get_height(self) -> float:
        return self._height

    def get_name(self) -> str:
        return self._name


class Flower(Plant):
    _color: str
    _bloomed: bool

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            growth_rate: float,
            color: str) -> None:
        super().__init__(
            name=name,
            height=height,
            days=days,
            growth_rate=growth_rate)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if not self._bloomed:
            print(f"{self._name.capitalize()} has not bloomed yet")
        else:
            print(f"{self._name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    _trunk_diameter: float

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            growth_rate: float,
            diameter: float) -> None:
        super().__init__(
            name=name,
            height=height,
            days=days,
            growth_rate=growth_rate)
        self._trunk_diameter = 0
        self.set_diameter(diameter)

    def show(self) -> None:
        super().show()
        print(f'Trunk diameter: {self._trunk_diameter:.1f}cm')

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name.capitalize()} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )

    def set_diameter(self, diameter: float) -> None:
        if diameter < 0:
            print(f"{self._name.capitalize()}:",
                  "Error, diameter can't be negative")
            return
        self._trunk_diameter = diameter


class Vegetable(Plant):
    _harvest_season: str
    _nutritional_value: int

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            growth_rate: float,
            season: str) -> None:
        super().__init__(
            name=name,
            height=height,
            days=days,
            growth_rate=growth_rate
        )
        self._harvest_season = season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season.capitalize()}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose: Flower = Flower(
        name="rose",
        height=15,
        days=10,
        growth_rate=0.2,
        color="red"
    )
    rose.show()
    print(f"[asking the {rose.get_name()} to bloom]")
    rose.bloom()
    rose.show()
    print("=== Tree")
    oak: Tree = Tree(
        name="oak",
        height=200,
        days=365,
        growth_rate=0.1,
        diameter=5
    )
    oak.show()
    print(f"[asking the {oak.get_name()} to produce shade]")
    oak.produce_shade()
    print("=== Vegetable")
    tomato: Vegetable = Vegetable(
        name="tomato",
        height=5,
        days=10,
        growth_rate=2.1,
        season="april"
    )
    tomato.show()
    print(f"[make {tomato.get_name()} grow and age for 20 days]")
    for day in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
