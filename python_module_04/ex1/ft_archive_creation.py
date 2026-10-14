#!/usr/bin/python3

import sys
import typing


def access_file(filename: str) -> str | None:
    file: typing.IO[str] | None = None
    print(f"Accessing file '{filename}'")
    try:
        file = open(filename, "r")
        print("---\n")
        text = file.read()
        print(text, end="\n---\n")
        return text
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file:
            file.close()
            print(f"File '{filename}' closed.")
    return None


def create_file(text: str) -> None:
    print("Transform data:")
    print("---\n")
    new_text: str = ""
    saved: bool = False
    for lines in text.splitlines():
        new_text += lines + "#\n"
    print(new_text, end="\n---\n")
    filename = input("Enter new file name (or empty): ")
    if filename == "":
        print("Not saving data.")
    else:
        file: typing.IO[str] | None = None
        try:
            file = open(filename, "w")
            print(f"Saving data to '{filename}'")
            file.write(new_text)
            saved = True
        except OSError as e:
            print(f"Failed to save data in file '{filename}': {e}")
        finally:
            if file:
                try:
                    file.close()
                    if saved:
                        print(f"Data saved in file '{filename}'.")
                except OSError as e:
                    print(f"Failed to save data in file '{filename}': {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        text = access_file(sys.argv[1])
        if text is not None:
            create_file(text)
