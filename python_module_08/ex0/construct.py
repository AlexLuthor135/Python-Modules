import sys
import os
import site

if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: Welcome to the construct")
        print("Current Python:", sys.executable)
        print("Virtual environment", os.path.basename(sys.prefix))
        print("Environment path:", sys.prefix)
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
    else:
        print("MATRIX STATUS: You're still plugged in")
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate")
        print(r"matrix_env\Scripts\activate")
        print("Then run this program again.")
    print("Package installation path:")
    for path in site.getsitepackages():
        print(path)
