#!/usr/bin/python3

import random

NAMES: list[str] = [
    'Alice', 'bob', 'Charlie', 'dylan',
    'Emma', 'Gregory', 'john', 'kevin', 'Liam'
]

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    capital_all: list[str] = [n.capitalize() for n in NAMES]
    capital_some: list[str] = [n for n in NAMES if n[0].isupper()]
    capital_dict: dict[str, int] = {
        n: random.randint(0, 1000) for n in capital_all
    }
    average: float = round(sum(capital_dict.values()) / len(capital_dict), 2)
    high_scorers: dict[str, int] = {
        n: value for n, value in capital_dict.items() if value > average
    }
    print(f'Initial list of players: {NAMES}')
    print(f'New list with all names capitalized: {capital_all}')
    print(f'New list of capitalized names only: {capital_some}\n')
    print(f'Score dict: {capital_dict}')
    print(f'Score average is {average}')
    print(f'High scores: {high_scorers}')
