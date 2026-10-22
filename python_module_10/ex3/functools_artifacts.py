from collections.abc import Callable
from typing import Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def enchant(power: int, element: str, target: str) -> str:
    return f"{element} enchantment on {target} with {power} power"


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    if operation == "add":
        return reduce(add, spells)
    if operation == "multiply":
        return reduce(mul, spells)
    if operation == "max":
        return reduce(max, spells)
    if operation == "min":
        return reduce(min, spells)
    raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = partial(base_enchantment, 50, "Fire")
    water = partial(base_enchantment, 50, "Water")
    ice = partial(base_enchantment, 50, "Ice")
    return {
        "fire": fire,
        "water": water,
        "ice": ice
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"
    return cast


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]

    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))
    print("Empty:", spell_reducer([], "add"))

    try:
        spell_reducer(spells, "divide")
    except ValueError as e:
        print("Error:", e)

    print("\nTesting partial enchanter...")
    enchantments = partial_enchanter(enchant)

    print(enchantments["fire"]("Sword"))
    print(enchantments["water"]("Staff"))
    print(enchantments["ice"]("Shield"))

    try:
        print(enchantments["sup"]("Sword"))
    except KeyError as e:
        print("Unknown enchantment:", e)

    print("\nTesting memoized fibonacci...")
    memoized_fibonacci.cache_clear()

    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("Cache before:", memoized_fibonacci.cache_info())
    print("Fib(15) again:", memoized_fibonacci(15))
    print("Cache after:", memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()

    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))


if __name__ == "__main__":
    main()
