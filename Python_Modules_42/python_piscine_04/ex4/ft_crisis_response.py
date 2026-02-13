#!/usr/bin/env python3

def ft_crisis_response():

    """
    This function calls to diferent errors we can have while reading/modifiying
    a document.

    Variables:
        - archives: name of the archives we are going to look for in the folder

    Functionality:
        - The function iterates though the archieves in the string archieves.
        It to each error whenever is found.
        - FileNotFoundError is called when the archive is not find in the
        folder.
        -PermissionError is called when you have not permision to read/ modify
        the archive.

    Returns:
        - This function doesn't returns anything.

    """

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    archives = [
         "lost_archive.txt",
         "classified_vault.txt",
         "standard_archive.txt",
    ]
    for archive in archives:
        try:
            with open(archive, "r") as vault:
                for line in vault:
                    print(line, end="")
                print("ROUTINE ACCESS: Attempting access to ", archive,
                      end="...\n")
                print("SUCCESS: Archive recovered -", line)
                print("STATUS: Normal operations resumed.\n")

        except FileNotFoundError:
            print("CRISIS ALERT: Attempting access to access", archive,
                  end="...\n")
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable.\n")
        except PermissionError:
            print("CRISIS ALERT: Attempting access to access", archive,
                  end="...\n")
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained.\n")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":

    ft_crisis_response()
