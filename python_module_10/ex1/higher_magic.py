from collections.abc import Callable

# def spell(target: str, power: int) -> str


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def power_up(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return power_up


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def check_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return check_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_all(target: str, power: int) -> list[str]:
        all_spells: list[str] = []
        for spell in spells:
            all_spells.append(spell(target, power))
        return all_spells
    return cast_all


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def enough_power(target: str, power: int) -> bool:
        return power >= 10

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result:", combined("Dragon", 10))

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print("Original:", fireball("Dragon", 10))
    print("Amplified:", mega_fireball("Dragon", 10))

    print("\nTesting conditional caster...")
    conditional = conditional_caster(enough_power, fireball)
    print("Valid:", conditional("Dragon", 15))
    print("Invalid:", conditional("Dragon", 5))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    for result in sequence("Dragon", 20):
        print(result)


if __name__ == "__main__":
    main()
