#!/usr/bin/env python3

import sys


def ft_stream_management():

    """
    This function is used to understand how to use the diferent outputs of
    of terminal usin the library sys.

    Variables:
        - user_name: name provided by the user to use the sys.stdin. input
        function has incorporated the call to the method.
        - report: string provided by the user by the sys.stdin.

    Functionality:
        - Recives and prints information in diferent output chanels.
        - Input recieves the information by the stdin (fd=0). It recieves
        the information writed in terminal by the user during the use of
        the program.
        -We print the standar strings using the standar output, calling it
        by sys.stdout.
        -We print the alert message by callin it through the error output
        sys.stderr.

    Returns:
        - This function doesn't returns anything.

    """

    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    user_id = input("Input Stream active. Enter archivist ID: ")
    report = input("Input Stream active. Enter status report: ")

    print(f"{{[}}STANDARD{{]}} Archive status from {user_id} : {report}",
          file=sys.stdout)
    print("{[}ALERT{]} System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("{[}STANDARD{]} Data transmission complete", file=sys.stdout)

    print()
    print("Three-channel communication test successful.")


if __name__ == "__main__":

    ft_stream_management()
