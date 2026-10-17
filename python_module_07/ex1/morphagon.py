from ex0.creature import Creature
from .transform_capability import TransformCapability


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} unleashes a devastating morph strike!"
        return f"{self._name} attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} stabilizes its form."
