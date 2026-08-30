#!/usr/bin/python3

class Plant:
    name: str
    height: int
    days: int

    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f'{self.name.capitalize()}:',
              f'{self.height:.1f}cm, {self.days} days old')


def main() -> None:
    rose = Plant(name="rose", height=25, days=30)
    sunflower = Plant(name="sunflower", height=80, days=45)
    cactus = Plant(name="cactus", height=15, days=120)
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    main()
