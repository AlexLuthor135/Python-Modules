#!/usr/bin/python3

import sys

inventory: dict[str, int] = {}


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    for argv in sys.argv[1:]:
        item_list: list[str] = argv.split(':')
        if len(item_list) != 2:
            print(f"Error - invalid parameter '{argv}'")
            continue
        if item_list[0] in inventory.keys():
            print(f"Redundant item '{item_list[0]}' - discarding")
            continue
        try:
            item_map: dict[str, int] = {item_list[0]: int(item_list[1])}
            inventory.update(item_map)
        except ValueError as e:
            print(f"Quantity error for '{item_list[0]}':", e)
    if len(inventory) == 0:
        print("Inventory is empty")
    else:
        nominals = len(inventory)
        quantity = sum(inventory.values())
        big: str = ""
        small: str = ""
        print(f"Got inventory: {inventory}")
        print(f"Item list: {list(inventory.keys())}")
        print(f"Total quantity of the {nominals} items: {quantity}")
        for item in inventory:
            if quantity != 0:
                print(f"Item {item} represents",
                      f"{round(100 / quantity * inventory[item], 1)}%")
            if not big or inventory[big] < inventory[item]:
                big = item
            if not small or inventory[small] > inventory[item]:
                small = item
        print(f"Item most abundant: {big} with quantity {inventory[big]}")
        print(f"Item least abundant: {small} with quantity {inventory[small]}")
        inventory.update({'magic_item': 1})
        print(f"Updated inventory: {inventory}")
