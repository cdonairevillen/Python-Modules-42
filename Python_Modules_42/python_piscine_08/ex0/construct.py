import sys
import os

if __name__ == "__main__":

    """Here is the main method to create a venv with python. If you run this
    script you will recieve the information to create and activate a new venv
    clean to work in it.

    venv creation workflow:
        - python3 -m venv "name"
        - source "name"/bin/activate
    _____________________________________________________________
    This activates the new venv. In bash you have not detector to know if
    the venv is active. To deactivate the isolate venv just write "deactivate"
    """

    current_python = sys.executable

    if sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print("Current Python", current_python)
        venv_path = sys.prefix
        venv_name = os.path.basename(venv_path)
        print("Virtual Environment:", venv_name)
        print("Environment Path:", venv_path)
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        site_packages = os.path.join(venv_path, "lib",
                                     f"python{sys.version_info.major}."
                                     f" {sys.version_info.minor}",
                                     "site-packages")
        print("Package installation path:")
        print(site_packages)
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print("Current Python", current_python)
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print(r"source matrix_env/bin/activate # On Unix")
        print(r"matrix_env/Scripts/activate # On Windows")
        print()
        print("Then run this program again.")
