#!/usr/bin/env python3


def ft_achievement_tracker():

    """
    Generates a random achieve setter for the 3 players listed below.
    Something interesting from set is taht it generates a random indexation
    if the elements they have inside, making some interesting effects in
    the achieve setting for each player.

    Variables:
        -all_achieves: array with all the achieves created for this
        project.
        -alice: set of achieves generated randomly from the 0 position to
        the 4th position.
        -bob: set of achieves generated randomly from the 1st position to
        the 5th position
        -charlie: set of achieves generated randomly from the second position
        to the seventh position.
        -"result_variable": store the results from the logic funtions below

    Functionality:
        - Once the sets are on, we print some comparatives to check:
            - All unique achieves the players have achieved
            - Wich achieves have any of the 3 players
            - Which achieves have just each of each player
            - Which achieves have one player who has not other of them.
            - Which achieves are unique for one player alone.

    Returns:
        - This function doesnt returns anything.
    """

    all_achieves = ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon',
                    'boss_slayer', 'collector', 'perfectionist', 'overlord']

    alice = set(all_achieves[:4])
    bob = set(all_achieves[1:5])
    charlie = set(all_achieves[2:7])

    all_unique = alice.union(bob).union(charlie)
    common = alice.intersection(bob).intersection(charlie)
    rare_alice = alice - bob.union(charlie)
    rare_bob = bob - alice.union(charlie)
    rare_charlie = charlie - alice.union(bob)
    rare = rare_alice.union(rare_bob).union(rare_charlie)
    alice_vs_bob = alice.intersection(bob)
    alice_unique = alice.difference(bob).difference(charlie)
    bob_unique = bob.difference(alice).difference(charlie)

    print("=== Achievement Tracker System ===\n")
    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)
    print("\n=== Achievement Analytics ===")
    print("All unique achievements:", all_unique)
    print("Total unique achievements:", len(all_unique))
    print("\n")
    print("Common to all players:", common)
    print("Rare achievements (1 player):", rare)
    print("\n")
    print("Alice vs Bob common:", alice_vs_bob)
    print("Alice unique:", alice_unique)
    print("Bob unique:", bob_unique)


if __name__ == "__main__":

    ft_achievement_tracker()
