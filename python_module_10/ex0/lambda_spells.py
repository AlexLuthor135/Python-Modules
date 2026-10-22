def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    new_artifacts = sorted(artifacts, key=lambda x: x["power"], reverse=True)
    return new_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    new_mages = filter(lambda x: x["power"] >= min_power, mages)
    return list(new_mages)


def spell_transformer(spells: list[str]) -> list[str]:
    new_spells = map(lambda x: "* " + x + " *", spells)
    return list(new_spells)


def mage_stats(mages: list[dict]) -> dict:
    strongest = max(mages, key=lambda x: x["power"])["power"]
    weakest = min(mages, key=lambda x: x["power"])["power"]
    average = round(sum(x["power"] for x in mages) / len(mages), ndigits=2)
    return {
        'max_power': strongest,
        'min_power': weakest,
        'avg_power': average,
    }


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "magic"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Magic Ring", "power": 40, "type": "accessory"},
    ]
    mages = [
        {"name": "Gandalf", "power": 90, "element": "fire"},
        {"name": "Merlin", "power": 50, "element": "water"},
        {"name": "Harry", "power": 30, "element": "air"},
    ]
    spells = ["fireball", "heal", "shield"]
    print("Testing artifact sorter...")
    for artifact in artifact_sorter(artifacts):
        print(f"{artifact['name']} ({artifact['power']} power)")
    print("\nTesting power filter...")
    for mage in power_filter(mages, 60):
        print(f"{mage['name']} ({mage['power']} power)")
    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))
    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print("Max power:", stats["max_power"])
    print("Min power:", stats["min_power"])
    print("Average power:", stats["avg_power"])


if __name__ == "__main__":
    main()
