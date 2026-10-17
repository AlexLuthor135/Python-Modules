from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(flame: CreatureFactory, aqua: CreatureFactory) -> None:
    print("Testing battle")
    fire = flame.create_base()
    water = aqua.create_base()
    print(fire.describe())
    print("vs")
    print(water.describe())
    print("fight!")
    print(fire.attack())
    print(water.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    test_factory(flame)
    test_factory(aqua)
    test_battle(flame, aqua)
