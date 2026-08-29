def ft_count_harvest_recursive() -> None:
    try:
        days: int = int(input("Days until harvest: "))
    except Exception as e:
        raise RuntimeError("Invalid input", e)

    def recursion(day: int) -> None:
        if day > days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        recursion(day + 1)
    recursion(1)
