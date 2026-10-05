#!/usr/bin/python3

import random

achievements: list[str] = [
    'Crafting Genius', 'Strategist', 'World Savior',
    'Speed Runner', 'Survivor', 'Master Explorer',
    'Treasure Hunter', 'Unstoppable', 'First Steps',
    'Collector Supreme', 'Untouchable', 'Sharp Mind',
    'Boss Slayer', '42 Student',
]


def gen_player_achievements() -> set[str]:
    amount: int = random.randint(6, 9)
    player_achievements: list[str] = random.sample(achievements, amount)
    return set(player_achievements)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    sam: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()
    print()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Sam: {sam}")
    print(f"Player Dylan: {dylan}")
    print()
    print(f"All distinct achievements: {set.union(alice, bob, sam, dylan)}")
    print()
    print(f'Common achievements: {set.intersection(alice, bob, sam, dylan)}')
    print()
    print(f"Only Alice has: {alice.difference(bob, sam, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, sam, dylan)}")
    print(f"Only Sam has: {sam.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, sam)}")
    print()
    achievements_set = set(achievements)
    print(f"Alice is missing: {achievements_set.difference(alice)}")
    print(f"Bob is missing: {achievements_set.difference(bob)}")
    print(f"Sam is missing: {achievements_set.difference(sam)}")
    print(f"Dylan is missing: {achievements_set.difference(dylan)}")
