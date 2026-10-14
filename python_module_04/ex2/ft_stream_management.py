#!/usr/bin/python3

import sys
import typing


def access_file(filename: str) -> str | None:
    file: typing.IO[str] | None = None
    sys.stdout.write(f"Accessing file '{filename}'\n")
    try:
        file = open(filename, "r")
        sys.stdout.write("---\n\n")
        text = file.read()
        sys.stdout.write(text + "\n---\n\n")
        return text
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
    finally:
        if file:
            try:
                file.close()
                sys.stdout.write(f"File '{filename}' closed.\n")
            except OSError as e:
                sys.stderr.write(
                    f"[STDERR] Failed to close file '{filename}': {e}\n"
                )
    return None


def create_file(text: str) -> None:
    sys.stdout.write("Transform data:\n")
    sys.stdout.write("---\n\n")
    new_text: str = ""
    saved: bool = False
    for lines in text.splitlines():
        new_text += lines + "#\n"
    sys.stdout.write(new_text + "\n---\n\n")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    filename = sys.stdin.readline().rstrip("\n")
    if filename == "":
        sys.stdout.write("Not saving data.\n")
    else:
        file: typing.IO[str] | None = None
        try:
            file = open(filename, "w")
            sys.stdout.write(f"Saving data to '{filename}'\n")
            file.write(new_text)
            saved = True
        except OSError as e:
            sys.stderr.write(
                f"[STDERR] Failed to save data in file '{filename}': {e}\n"
            )
        finally:
            if file:
                try:
                    file.close()
                    if saved:
                        sys.stdout.write(f"Data saved in file '{filename}'.\n")
                except OSError as e:
                    sys.stderr.write(
                        f"[STDERR] Failed to save data in file "
                        f"'{filename}': {e}\n"
                    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stdout.write("Usage: ft_stream_management.py <file>\n")
    else:
        sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
        text = access_file(sys.argv[1])
        if text is not None:
            create_file(text)
