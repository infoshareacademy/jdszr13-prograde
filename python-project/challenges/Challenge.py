import matplotlib.pyplot as plt

class Challenge:

    player_pokemons_scores = {}
    total_wins = 0

    def __init__(self, player_team, team_name, possible_opponents, type_of_challange):
        self.player_team = player_team.reset_index()
        self.team_name = team_name
        self.possible_opponents = possible_opponents
        self.type_of_challange = type_of_challange

    def choose_random_opponent(self):
        return self.possible_opponents.sample(1)
    
    def create_pokemon_individual_score_table(self):
        for i in range(len(self.player_team)):
            self.player_pokemons_scores[self.player_team['name'].iloc[i]] = 0

    def clear_scores(self):
        self.total_iterations = 0
        self.total_wins = 0
        self.player_pokemons_scores = {}

    def increase_overall_score(self):
        self.total_wins += 1
        return self.total_wins
    
    def increase_pokemon_individual_score(self, i):
        self.player_pokemons_scores[self.player_team['name'].iloc[i]] += 1
        return self.player_pokemons_scores

    def perform_challenge(self):
        self.clear_scores()
        self.create_pokemon_individual_score_table()
        for i in range(len(self.player_team)):
            for _ in range(100):
                opponent = self.choose_random_opponent()
                if self.player_team[self.type_of_challange].iloc[i] > opponent[self.type_of_challange].iloc[0]:
                    self.increase_overall_score()
                    self.increase_pokemon_individual_score(i)
        return (self.total_wins, self.player_pokemons_scores)

    # def show_results(self):
    #     x = self.player_pokemons_scores.keys()
    #     y = self.player_pokemons_scores.values()
                          
    #     # fig, ax = plt.subplots()
        
    #     plot = plt.bar(x,y)
    #     plt.title(f'Challenge: {self.type_of_challange}')
    #     return plot

    #     # if self.type_of_challange == 'hp':
    #     #     fig.suptitle(f'Number of wins in the endurance challenge for team: {self.team_name}.')
    #     # else: 
    #     #     fig.suptitle(f'Number of wins in {self.type_of_challange} challenge for team: {self.team_name}.')

    #     # ax.bar(x, y, color='orange')


