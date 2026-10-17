
from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex0.creature import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def tournament(setup: list[tuple[
        CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(setup)} opponents involved")
    creatures: list[Creature] = []
    for i in range(len(setup)):
        creatures.append(setup[i][0].create_base())
    for i in range(len(setup)):
        for j in range(i + 1, len(creatures)):
            print("\n* Battle *")
            creature1 = creatures[i]
            creature2 = creatures[j]
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")
            try:
                print(setup[i][1].act(creature1))
                print(setup[j][1].act(creature2))
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    tournament([(flame, normal), (heal, defensive)])
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    tournament([(flame, aggressive), (heal, defensive)])
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), "
          "(Transform+Aggressive) ]")
    tournament([(aqua, normal), (heal, defensive), (transform, aggressive)])
