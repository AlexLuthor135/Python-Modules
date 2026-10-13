#!/usr/bin/python3

import random
import typing

NAMES: list[str] = ['alice', 'dylan', 'bob', 'charlie', 'arnold', 'sam']
ACTIONS: list[str] = ['run', 'grab', 'fall', 'sleep', 'pray', 'laugh', 'eat']
generated_list: list[tuple[str, str]] = []


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(NAMES)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
        generated_list: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while len(generated_list) != 0:
        random_tuple = random.choice(generated_list)
        generated_list.remove(random_tuple)
        yield random_tuple


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    counter: int = 0
    events: typing.Generator[tuple[str, str], None, None] = gen_event()
    while counter != 1000:
        event = next(events)
        print(f'Event {counter}: Player {event[0]} did action {event[1]}')
        counter += 1
    for _ in range(10):
        generated_list.append(next(events))
    print(f'Built list of 10 events: {generated_list}')
    events = consume_event(generated_list)
    for random_tuple in events:
        print(f'Got event from list: {random_tuple}')
        print(f'Remains in list: {generated_list}')
