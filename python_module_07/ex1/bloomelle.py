from ex0.creature import Creature
from .heal_capability import HealCapability


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self._name} heals itself and others for a large amount"
