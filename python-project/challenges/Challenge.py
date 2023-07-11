class Challenge:

    # player_pokemons = {} this should count points for each pokemon
    total_wins = 0
    total_iterations = 0
    
    def __init__(self, player_team, possible_opponents, type_of_challange):
        self.player_team = player_team.reset_index()
        self.possible_opponents = possible_opponents
        self.type_of_challange = type_of_challange

    def choose_random_opponent(self):
        return self.possible_opponents.sample(1)
    
    def create_score_table(self):
        # add pokemons to player_pokemons dictionary
        return
    
    def perform_challenge(self):

        for i in range(len(self.player_team)):
            for _ in range(100):
                opponent = self.choose_random_opponent()

                if self.player_team[self.type_of_challange].iloc[i] > opponent[self.type_of_challange].iloc[0]:
                    self.total_wins += 1
            total_iterations += 1
        return self.total_wins

    # save_results

    # show_results

