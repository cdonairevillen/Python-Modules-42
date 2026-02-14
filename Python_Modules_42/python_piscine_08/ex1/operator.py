import sys

if __name__ == "__main__":

    """
    pip workflow:
        - python3 -m venv "name"
        - source "name"/bin/activate
        - pip install -r requirements.txt
        - python3 operator.py
        _________________________________________________
        This generates and installs all dependencies in the venv via pip

    poetry workflow:
        - poetry install
        - poetry run python3 operator.py
        _________________________________________________
        Poetry generates an isolated venv defined by the .toml file.
        By using "poetry" as a runner, you execute the script in the
        poetry venv.

    **NOTE: you may have memory space problems while creating a new venv
    with Poetry. In that case, you'll need to delete old virtual environments
    using:

        - rm -rf ~/.cache/poetry/virtualenvs
        - poetry cache clear --all
    """

    print("OPERATOR STATUS: Loading programs...")
    print()
    print("Checking dependencies:")

    total = 0

    try:
        # Pandas is a library with methods to analyze structured data
        import pandas
        total += 1
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ImportError:
        print("[KO] pandas library not found in the venv")

    try:
        # Requests is used to extract info from APIs and web services
        import requests
        total += 1
        print(f"[OK] requests ({requests.__version__}) - Network access ready")
    except ImportError:
        print("[KO] requests library not found in the venv")

    try:
        # Matplotlib is a visualization library used to create graphs
        import matplotlib
        import matplotlib.pyplot as pyp
        total += 1
        print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization"
              " ready")
    except ImportError:
        print("[KO] matplotlib library not found in the venv")

    try:
        # NumPy is the base math library for Python
        import numpy
        total += 1
        print(f"[OK] numpy ({numpy.__version__}) - Math library ready")
    except ImportError:
        print("[KO] numpy library not found in the venv")

    print()

    if total != 4:
        print("Some dependencies are missing.")
        print("Install them using:")
        print("pip install -r requirements.txt")
        print("or:")
        print("poetry install")
        sys.exit(1)

    n = 0

    try:
        res = requests.get("https://jsonplaceholder.typicode.com/posts",
                           timeout=5)
        res.raise_for_status()
        external_data = res.json()

        for _ in external_data:
            n += 1

        values = [len(item["body"]) for item in external_data[:n]]

    except requests.exceptions.RequestException:
        print("Failed to fetch external data. Continuing with proxies")
        n = 1000
        values = numpy.random.randn(n)

    print("\nAnalyzing Matrix Data...")
    print(f"Processing {n} data points...")

    steps = numpy.arange(n)

    data = pandas.DataFrame({
        "step": steps,
        "value": values
    })

    median_value = data["value"].median()

    print("Generating visualization...")

    pyp.figure()
    pyp.plot(data["step"], data["value"], label="Matrix signal")

    pyp.axhline(y=median_value,
                linestyle="--",
                label=f"Median value = {median_value:.2f}")
    pyp.xlabel("Step")
    pyp.ylabel("Value")
    pyp.title("Evolution of IA")
    pyp.legend(title=f"Median: {median_value:.2f}")
    pyp.savefig("Evolution_of_IA.png")
    pyp.close()

    print()
    print("Analysis complete!")
    print("Results saved in: Evolution_of_IA.png")
