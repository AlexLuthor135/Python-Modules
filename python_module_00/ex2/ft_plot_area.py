def ft_plot_area() -> None:
    try:
        length: int = int(input("Enter length: "))
        width: int = int(input("Enter width: "))
    except Exception as e:
        raise RuntimeError("Invalid input: ", e)
    print("Plot area:", length * width)
