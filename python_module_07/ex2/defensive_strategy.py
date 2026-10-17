from typing import cast
from .battle_strategy import BattleStrategy
from ex0.creature import Creature
from ex1.heal_capability import HealCapability
from .invalid_strategy import InvalidStrategyError


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError("Creature cannot heal")
        h = cast(HealCapability, creature)
        return f"{creature.attack()}\n{h.heal()}"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
