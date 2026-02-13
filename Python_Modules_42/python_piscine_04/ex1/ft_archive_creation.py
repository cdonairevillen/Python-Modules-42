#!/usr/bin/env python3

def ft_archive_creation():

    """
    This function uses the function open to create a new document with the
    string told in the proyect.

    Variables:
        - imput: name of the document to create.
        - strings: Information that will be writed in the file.

    Functionality:
        - Creates or modify a document named "new_discovery.txt". It writes
        each of the string in strings in new lines and print them in by
        by terminal. Then, close the archive.

    Returns:
        - This function doesn't returns anything.

    """

    name = "new_discovery.txt"

    strings = ["{[}ENTRY 001{]} New quantum algorithm discovered\n"
               "{[}ENTRY 002{]} Efficiency increased by 347%\n"
               "{[}ENTRY 003{]} Archived by Data Archivist trainee\n"]

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    print("Initializing new storage unit: new_discovery.txt")

    text = open(name, 'w')
    if text is None:
        print("ERROR: Storage unit could not be created.")

    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    for line in strings:
        text.write(line)
        print(line, end="")

    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive {name} ready for long-term preservation.")
    text.close()


if __name__ == "__main__":

    ft_archive_creation()
