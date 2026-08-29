def ft_count_harvest_iterative() -> None:
    try:
        days: int = int(input("Days until harvest: "))
    except Exception as e:
        raise RuntimeError("Invalid input", e)
    day: int = 1
    while day != days + 1:
        print(f"Day {day}")
        day += 1
    print("Harvest time!")
