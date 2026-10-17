from ex0.creature import Creature
from .transform_capability import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} performs a boosted strike!"
        return f"{self._name} attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} returns to normal."
