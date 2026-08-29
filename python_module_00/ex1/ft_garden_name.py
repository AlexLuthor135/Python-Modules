def ft_garden_name() -> None:
    try:
        name: str = input("Enter garden name: ")
    except Exception as e:
        raise RuntimeError("Invalid type: ", e)
    print(f'Garden: {name}')
    print('Status: Growing well!')
