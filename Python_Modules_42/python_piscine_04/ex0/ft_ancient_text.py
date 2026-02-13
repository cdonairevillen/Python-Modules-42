#!/usr/bin/env python3

def ft_ancient_text():

    """
    This function is thought to learn how to use the open function in Python
    for reading inside document information.

    Variables:
        - imput: name of the .txt who is going to be red
        - text: variable that recieve the information from open

    Functionality:
        - Take the info from the document, iterate line by line an prints the
        information of each of the iteration. Then close the archieve.

    Returns:
        - This function doesnt returns anything.

    """

    imput = 'ancient_fragment.txt'

    text = open(imput, "r")

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    print(f"Accessing Storage Vault: {imput}")
    print("Connection established...\n")

    print("RECOVERED DATA:\n")

    a = text.read()
    print(a)

    print()
    print("\nData recovery complete. Storage unit disconnected.")

    text.close()


if __name__ == "__main__":

    ft_ancient_text()
