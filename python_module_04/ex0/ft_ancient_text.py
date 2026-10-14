#!/usr/bin/python3

import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        filename: str = sys.argv[1]
        file: typing.IO[str] | None = None
        print(f"Accessing file '{filename}'")
        try:
            file = open(filename)
            print("---\n")
            text = file.read()
            print(text, end="\n---\n")
        except OSError as e:
            print(f"Error opening file '{filename}': {e}")
        finally:
            if file:
                file.close()
                print(f"File '{filename}' closed.")
