from typing import cast
from .battle_strategy import BattleStrategy
from ex0.creature import Creature
from ex1.transform_capability import TransformCapability
from .invalid_strategy import InvalidStrategyError


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError("Creature cannot transform")
        t = cast(TransformCapability, creature)
        return f"{t.transform()}\n{creature.attack()}\n{t.revert()}"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)
