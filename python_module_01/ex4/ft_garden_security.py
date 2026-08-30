#!/usr/bin/python3

class Plant:
    _name: str
    _height: float
    _days: int
    _growth_rate: float
    _initial_height: float

    def __init__(self, name: str, height: float, days: int, growth_rate: float
                 ) -> None:
        self._name = name
        self._growth_rate = growth_rate
        self._initial_height = 0
        self._days = 0
        self._height = 0
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


def main() -> None:
    print("=== Garden Security System ===")
    rose: Plant = Plant(name="rose", height=25, days=30, growth_rate=0.8)
    print("Plant created:", end=" ")
    rose.show()
    rose.set_height(20)
    print("Height updated:", rose.get_height())
    rose.set_age(20)
    print("Age updated:", rose.get_age())
    rose.set_height(-1)
    rose.set_age(-1)
    print("Current state:", end=" ")
    rose.show()


if __name__ == "__main__":
    main()
