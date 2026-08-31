#!/usr/bin/python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    if operation_number == 1:
        1 / 0
    if operation_number == 2:
        open("./non/existent/file")
    if operation_number == 3:
        "abc" + 1
    print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    try:
        garden_operations(0)
    except (ValueError, ZeroDivisionError,
            FileNotFoundError, TypeError) as e:
        print("Caught Error:", e)
    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError", e)
    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)
    print("Testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as e:
        print("Caught TypeError:", e)
    print("Testing operation 4...")
    try:
        garden_operations(4)
    except Exception as e:
        print("Caught Exception:", e)
    print("All error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
