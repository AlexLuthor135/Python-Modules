#!/usr/bin/python3

def secure_archive(filename: str, action: str = "r", content: str | None = None
                   ) -> tuple[bool, str]:
    if action not in ("w", "r"):
        return (False, "Invalid action")
    try:
        if action == "w" and content is None:
            return (False, "No content provided")
        with open(filename, action) as file:
            if action == "r":
                text: str = file.read()
            elif action == "w":
                file.write(content)
                return (True, "Content successfully written to file")
    except OSError as e:
        return (False, str(e))
    return (True, text)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    result: tuple[bool, str]
    print("Using 'secure_archive' to read from a nonexistent file:")
    result = secure_archive('/not/existing/file')
    print(result)
    print("Using 'secure_archive' to read from an inaccessible file:")
    result = secure_archive('/etc/master.passwd')
    print(result)
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive('./text.txt')
    print(result)
    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        result = secure_archive('./text_copy.txt', "w", result[1])
        print(result)
