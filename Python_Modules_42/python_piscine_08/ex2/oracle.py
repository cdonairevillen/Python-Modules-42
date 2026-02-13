import os

if __name__ == "__main__":

    """
    For production overwrite, apply by console

    {all the environment keys you want(MATRIX_MODE=production is mandatory)} +
    python3 oracle.py
    """

    print("ORACLE STATUS: Reading the Matrix...")
    path = ".env"

    env_read = False
    env_loaded = False
    if os.path.exists(path):
        with open(path) as env:
            for line in env:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip()
                    env_read = True
                    if key not in os.environ:
                        os.environ[key] = value
                        env_loaded = True

    mode = os.environ.get("MATRIX_MODE", "development")
    url = os.environ.get("DATABASE_URL", "")
    key = os.environ.get("API_KEY", "")
    level = os.environ.get("LOG_LEVEL", "")
    endpoint = os.environ.get("ZION_ENDPOINT", "")

    print()
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    if url:
        print("Database: Connected to local instance")
    else:
        print("Database: You coudn't connected to a database")
    if key:
        print("API Access: Authenticated")
    else:
        print("API Access: (not set)")
    if level:
        print(f"Log Level: {level}")
    else:
        print("Log Level: (not set)")
    if endpoint:
        print(f"Zion Network: {endpoint}")
    else:
        print("Zion Network: (not set)")
    print()

    if key == "":
        print("[WARNING] No API key detected")
    else:
        print("[OK] No hardcoded secrets detected")

    if env_loaded:
        print("[OK] .env file properly configured")
    elif env_read and env_loaded is False:
        print("[INFO] .env file found but not used."
              "Using environment variables.")
    else:
        print("[WARNING] .env file missing and not environment"
              " variables seted")

    if mode == "production":

        if not url or not key or not endpoint or not level:
            print("[WARNING] Some production variables are missing!")
        else:
            print("[OK] Production overrides available")
    else:
        print("[INFO]Not production mode enabled")

    print()
    print("The Oracle sees all configurations")
