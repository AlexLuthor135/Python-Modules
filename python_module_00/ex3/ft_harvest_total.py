def ft_harvest_total() -> None:
    numbers = []
    while len(numbers) != 3:
        try:
            numbers.append(int(input(f"Day {len(numbers) + 1} harvest: ")))
        except Exception as e:
            raise RuntimeError("Invalid input: ", e)
    if len(numbers) != 3:
        raise RuntimeError("The size of the list is incorrect")
    print(f"Total harvest: {numbers[0] + numbers[1] + numbers[2]}")
