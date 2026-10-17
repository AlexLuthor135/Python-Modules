from alchemy.potions import strength_potion
import elements
from ..elements import create_air


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew "
            f"'{create_air()}' and '{strength_potion()}' "
            f"mixed with '{elements.create_fire()}'")
