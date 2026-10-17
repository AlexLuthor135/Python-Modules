import importlib


def compare_dependencies() -> None:
    print("\nInstalled package versions:")
    for name in ["numpy", "pandas", "matplotlib"]:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"{name}: {version}")

    print("\nDependency management comparison:")
    print("pip: installs dependencies from requirements.txt")
    print("Poetry: manages dependencies using pyproject.toml")
    print("Poetry: locks exact versions in poetry.lock")


def check_dependencies() -> bool:
    modules: list[str] = ["numpy", "pandas", "matplotlib"]
    for m in modules:
        try:
            importlib.import_module(m)
            print(f"[OK] {m}")
        except ModuleNotFoundError as e:
            print(f"Error loading module: {e}")
            print("Install dependencies using:")
            print("pip install -r requirements.txt")
            print("or")
            print("poetry install")
            return False
    return True


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    if check_dependencies():
        compare_dependencies()
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        numbers = np.random.default_rng()
        data = numbers.integers(0, 100, size=1000)
        print("Analyzing Matrix data...")
        print(f"Processing {data.size} data points...")
        print(data.mean())
        print(data.max())
        print(data.min())
        print(data.sum())
        df = pd.DataFrame({"value": data})
        print(df.describe())
        print("Generating visualization...")
        plt.hist(df["value"], bins=20)
        plt.title("Matrix Data Analysis")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.savefig("matrix_analysis.png")
        plt.close()
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
