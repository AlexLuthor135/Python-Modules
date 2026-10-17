from ex0.creature import Creature
from .heal_capability import HealCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"
