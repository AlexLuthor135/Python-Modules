def ft_water_reminder() -> None:
    try:
        days: int = int(input("Days since last watering: "))
    except Exception as e:
        raise RuntimeError("Invalid input", e)
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
