#!/usr/bin/env python3

def ft_analytics_dashboard():

    from data_generator import PixelDataGenerator

    """
    This program extrac from data_generator a string of data that will be
    processed using comprehensions
    Variables:
        -generator : encapsules the class imported
        -players : extract from generate_exercise_data(6) the information used
        to do the exercice
        -top_performers : list that saves the informatio of the players with
        score above 2000
        -score_doubled: list of all the scores multiplied by 2
        -active players: list of all the players with more than 25 sessions
        played.
        -player_score: dictionary that saves from players the player and his
        total score.
        -score_cat: dictionary that clasficates the score of each player in
        'high' >= 4000; 3000 <= 'medium' < 4000 ; 'low' < 3000
        -achieves_count: dictionary that saves from players the player and the
        amount of achieves he has.
        -unique_players: creates a set with each unique player registered.
        -u_acheves: creates a set with all the achieves registered by all the
        players
        -act_regions: creates a set with all the regions registered by each
        active player.
        -top_perform: looks for the highest score in players
        -top_score: saves the total score of the top_perform
        -top_achieves: saves the achieve_count from the chosen player
    Functionality:
        -just reads eficiently the information from the dictionary provided. It
        sets some extra information required to make the output more similar to
        the propossed in the subject.
    Return:
        -This function doesn't return anything
    """

    def set_region(players):

        """
        This function creates and set the regions for prin in the act_regions
        variable.
        Variable:
            -regions: a list of list that has all the instances we are using in
            our region setter
            -i: iterator
        Functionality:
            -we iterate for player in our players dictionary and set a new key
            'region' taht has one of the regios setted in the region list.
        Return:
            -this function doesn't return anything.
        """

        regions = [["north"], ["east"], ["west"], ["south"], ["central"]]

        i = 0
        for player in players:
            players[player]['region'] = regions[i]
            i += 1
            if i >= 5:
                i = 0

    def set_achieves(players):

        """
        This function creates and set the achieves for prin in the u_acieves
        variable.
        Variable:
            -all achieves: a list of list that has all the instances we are
            using in our set achieves
            -i: iterator
        Functionality:
            -we iterate for player in our players dictionary and set 'i' new
             achieves to a new 'achieves' kew
        Return:
            -this function doesn't return anything.
        """

        all_achieves = ['first_kill', 'level_10', 'treasure_hunter',
                        'speed_demon', 'boss_slayer', 'collector',
                        'perfectionist', 'overlord']

        i = 0
        for player in players:
            players[player]['achieves'] = all_achieves[:i]
            i += 1
            if i >= 8:
                i = 0

    generator = PixelDataGenerator(seed=42)
    data = generator.generate_exercise_data(6)
    players = data['players']
    set_region(players)
    set_achieves(players)
    print(players)

    print("\n=== List Comprehension Examples ===")
    # Generates a list for the top perfomers trough the dictionary "players"
    top_performers = [player for player in players
                      if players[player]['total_score'] > 2000]
    print("High scorers(<2000):", top_performers)
    # Generates a list and doble the score of each player in the dictionary
    # players
    score_doubled = [players[player]['total_score'] * 2 for player in players]
    print("Scores doubled:", score_doubled)
    # Generates a list with the most ative players
    active_players = [player for player in players
                      if players[player]['sessions_played'] > 25]
    print("Active Players:", active_players)

    print("\n=== Dict Comprehension Examples ===")
    # Generates a dictionary with all the players and their scores
    player_scores = {player: players[player]['total_score']
                     for player in players}
    print("Player Scores:", player_scores)
    # Generates a dictionary with the sum of each type of score between
    # the active players
    score_cat = {
        'high': sum(1 for player in active_players
                    if players[player]['total_score'] >= 4000),
        'medium': sum(1 for player in active_players
                      if 3000 <= players[player]['total_score'] < 4000),
        'low': sum(1 for player in active_players
                   if players[player]['total_score'] < 3000)
                    }
    print("Score Categroies:", score_cat)
    # Generates a dictionary with each player and the count of achieves
    # he has.
    achieves_count = {player: players[player]['achievements_count']
                      for player in active_players}
    print("Achievement Counts:", achieves_count)

    print("\n=== Set Comprehension Example} ===")
    # Creates a sset with all the players registered in the game
    unique_players = {player for player in players}
    print("Unique Players:", unique_players)
    # Creates a set with all the achieves in the players posesion
    u_achieves = {achieves for player in players for
                  achieves in players[player]['achieves']}
    print("Unique Achievements:", u_achieves)
    # Creates a set with all the regions registered between the active
    # players
    act_regions = {region for player in active_players for
                   region in players[player]['region']}
    print("Active Regions:", act_regions)

    print("\n=== Combined Analysis ===")
    print("Total players", len(unique_players))
    print("Total unique achievements:", len(u_achieves))
    print(f"Average score: {((sum(score_doubled))/2)/len(unique_players):.1f}")
    top_perform = max(top_performers)
    top_score = players[top_perform]['total_score']
    top_achieves = players[top_perform]['achievements_count']
    print(f"Top performer:{top_perform} ({top_score} "
          f"score, {top_achieves} achieves)")


if __name__ == "__main__":

    ft_analytics_dashboard()
