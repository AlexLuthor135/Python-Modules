from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        first = perf_counter()
        result = func(*args, **kwargs)
        second = perf_counter()
        print(f"Spell completed in {second - first:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power: Any = kwargs.get("power")
            if power is None:
                power = args[-1]
            if min_power > power:
                return "Insufficient power for this spell"
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    if max_attempts > 0:
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                attempt: int = 0
                while attempt != max_attempts:
                    try:
                        result = func(*args, **kwargs)
                        return result
                    except Exception:
                        attempt += 1
                        if attempt != max_attempts:
                            print("Spell failed, retrying...",
                                  f"(attempt {attempt}/{max_attempts})")
                return f"Spell casting failed after {max_attempts} attempts"
            return wrapper
        return decorator
    raise ValueError("Attempts must be positive")


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        new_name = name.replace(" ", "")
        return new_name.isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str) -> str:
        return f"Fireball hits {target}!"

    print("Result:", fireball("Dragon"))

    print("\nTesting power validator...")

    @power_validator(10)
    def lightning(target: str, power: int) -> str:
        return f"Lightning hits {target} with {power} power"

    print(lightning("Dragon", 15))
    print(lightning("Dragon", 5))
    print(lightning("Dragon", power=10))

    print("\nTesting retrying spell...")

    attempts = 0

    @retry_spell(3)
    def unstable_spell() -> str:
        nonlocal attempts
        attempts += 1

        if attempts < 3:
            raise ValueError("Spell failed")

        return "Spell successfully cast!"

    print(unstable_spell())

    print("\nTesting complete spell failure...")

    @retry_spell(3)
    def broken_spell() -> str:
        raise ValueError("Spell always fails")

    print(broken_spell())

    print("\nTesting MageGuild...")

    print("Valid name:", MageGuild.validate_mage_name("Gandalf"))
    print("Invalid name:", MageGuild.validate_mage_name("Al1"))

    guild = MageGuild()

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fireball", 5))


if __name__ == "__main__":
    main()
