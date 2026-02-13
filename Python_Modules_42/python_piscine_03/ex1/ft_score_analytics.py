#!/usr/bin/env python3

import sys


def ft_argv_control():

    """
    Track by argument the entry of scores from x number of players:

    Variables:
        - scores: array that groups all the scores from sys.argv from
        the position to the position n-1

    Functionality:
        - ensures if the len of sys.argv is grater then 1.
        - prints some mathematical ecuations with the information provided
        - It raises a ValueError if anything goes wrong.

    Returns:
        - This function doesnt returns anything.
    """

    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No arguments provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2>")
    else:
        try:
            scores = [int(arg) for arg in sys.argv[1:]]
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total Score: {sum(scores)}")
            print(f"Average Score: {sum(scores)/len(scores):.0f}")
            print("High Score:", max(scores))
            print("Lowest Score:", min(scores))
            print(f"Score Range : {max(scores) - min(scores)}")
        except ValueError as e:
            print(f"ERROR: all scores must be integers({e})")


if __name__ == "__main__":
    ft_argv_control()
