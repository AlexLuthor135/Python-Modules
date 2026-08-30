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
        self._stats = self.Stats()

    def show(self) -> None:
        print(f'{self._name.capitalize()}:',
              f'{self._height:.1f}cm, {self._days} days old')
        self._stats._increment_show()

    def age(self, days: int = 1) -> None:
        self._days += days
        self._stats._increment_age()

    def grow(self) -> None:
        self._height += self._growth_rate
        self._stats._increment_grow()

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

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls(
            name="Unknown plant",
            days=0,
            height=0,
            growth_rate=0,
        )

    def display_stats(self) -> None:
        self._stats.display()

    class Stats:
        _grow_count: int
        _age_count: int
        _show_count: int

        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def _increment_grow(self) -> None:
            self._grow_count += 1

        def _increment_age(self) -> None:
            self._age_count += 1

        def _increment_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show"
            )


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


class Seed(Flower):
    _seeds: int

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
            growth_rate=growth_rate,
            color=color)
        self._seeds = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42


class Tree(Plant):
    _trunk_diameter: float
    _shades: int

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
        self._shades = 0
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
        self._shades += 1

    def set_diameter(self, diameter: float) -> None:
        if diameter < 0:
            print(f"{self._name.capitalize()}:",
                  "Error, diameter can't be negative")
            return
        self._trunk_diameter = diameter

    def display_stats(self) -> None:
        super().display_stats()
        print(f"{self._shades} shade")


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

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value += days


def display_stats(plant: Plant) -> None:
    plant.display_stats()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.is_older_than_year(30))
    print("Is 400 days more than a year? ->", Plant.is_older_than_year(400))
    print("=== Flower")
    rose: Flower = Flower(
        name="rose",
        height=15,
        days=10,
        growth_rate=8,
        color="red"
    )
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("=== Tree")
    oak: Tree = Tree(
        name="oak",
        height=200,
        days=365,
        growth_rate=0.1,
        diameter=5
    )
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)
    print("=== Seed")
    sunflower: Seed = Seed(
        name="sunflower",
        height=80,
        days=45,
        growth_rate=30,
        color="yellow"
    )
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)
    print("=== Anonymous")
    anonymous: Plant = Plant.create_anonymous()
    anonymous.show()
    print("[statistics for Unknown plant]")
    display_stats(anonymous)


if __name__ == "__main__":
    main()
