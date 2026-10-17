from .creature_factory import CreatureFactory
from .creature import Creature
from .aquabub import Aquabub
from .torragon import Torragon


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
