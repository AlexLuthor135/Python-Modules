def ft_plant_age() -> None:
    try:
        age: int = int(input("Enter plant age in days: "))
    except Exception as e:
        raise RuntimeError("Invalid input", e)
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
