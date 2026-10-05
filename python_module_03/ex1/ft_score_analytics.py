#!/usr/bin/python3

import sys


def score_analytics() -> None:
    score_list: list[int] = []
    for score in sys.argv[1:]:
        try:
            number = int(score)
            number_list = [number]
            score_list = score_list + number_list
        except ValueError:
            print(f"Invalid parameter: '{score}'")
    if len(score_list) == 0:
        print("No scores provided.", end=" ")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f'Scores processed: {score_list}')
        print(f'Total players: {len(score_list)}')
        print(f'Total score: {sum(score_list)}')
        print(f'Average score: {sum(score_list) / len(score_list)}')
        print(f'High score: {max(score_list)}')
        print(f'Low score: {min(score_list)}')
        print(f'Score range: {max(score_list) - min(score_list)}')


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_analytics()
