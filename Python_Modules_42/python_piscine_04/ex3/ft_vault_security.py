#!/usr/bin/env python3

def ft_vault_security():

    """
    This function is used to show how to modify/read documents using the
    operator with, dont needidng the close function to end the use of the
    te document.

    Variables:
        - strings: all the string that are going to be used to be written in
        the document.

    Functionality:
        -As with a normal open function, "with" works by a secure method.
        if the funtion breaks in any point, the operator closes the archive
        automatically. We can use it to rear and write the archive.
        -The secure methos with use is to create an object with the
        information. As how are designed the object, they get destroyed in
        the moment the program stops, so this dont left any memory accesible
        even not properly closing the file.

    Returns:
        - This function doesn't returns anything.

    """

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    string = ["[CLASSIFIED] New security protocols archived.\n",
              "[CLASSIFIED] Old security protocols actualized.\n",]

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    with open("classified_data.txt", "r") as vault:
        print(vault.read())

    print()
    print("\nSECURE PRESERVATION:")
    with open("security_protocols.txt", "w") as vault:
        for statement in string:
            vault.write(statement)
            print(statement, end="")

    print("Vault automatically sealed upon completion\n")

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":

    ft_vault_security()
