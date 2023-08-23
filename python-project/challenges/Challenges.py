import matplotlib.pyplot as plt

class Challenges:
    '''
        Class that creates challenges for given pokemon teams

        |player_team            pandas dataframe with player chosen pokemons
        |team_name              string with team's name
        |possible_opponents     pandas dataframe with opponent pokemons
    '''

    pokemon_score = {}
    scores_from_all_challenges = {}
    current_challenge_wins = 0
    total_wins = 0
    challenge_types = ['attack', 'defense', 'hp', 'sp_attack', 'sp_defense', 'speed']

    def __init__(self, player_team:str, team_name, possible_opponents):
        self.player_team = player_team.reset_index()
        self.team_name = team_name
        self.possible_opponents = possible_opponents

    def choose_random_opponent(self):
        return self.possible_opponents.sample(1)
    
    def create_pokemon_individual_score_table(self):
        for i in range(len(self.player_team)):
            self.pokemon_score[self.player_team['name'].iloc[i]] = 0

    def clear_score(self):
        self.current_challenge_wins = 0

    def increase_current_score(self):
        self.current_challenge_wins += 1
    
    def clear_total_score(self):
        self.total_wins = 0
    
    def increase_pokemon_individual_score(self, i):
        self.pokemon_score[self.player_team['name'].iloc[i]] += 1
        return self.pokemon_score

    def perform_challenge(self, challenge_type):

        self.create_pokemon_individual_score_table()
        self.clear_score()

        for i in range(len(self.player_team)):
            for _ in range(100):
                opponent = self.choose_random_opponent()
                if self.player_team[challenge_type].iloc[i] > opponent[challenge_type].iloc[0]:
                    self.increase_current_score()
                    self.increase_pokemon_individual_score(i)
        
        return (self.current_challenge_wins, self.pokemon_score)
    
    def perform_all_challenges(self):
        for challenge_type in self.challenge_types:
            score = self.perform_challenge(challenge_type)
            self.total_wins += score[0]
            print(score[1])
            self.scores_from_all_challenges[challenge_type] = score[1]
            print(self.scores_from_all_challenges)

        percentage_of_wins = int(self.total_wins/3600*100)
        print(f'Out of possible 3600 wins, team {self.team_name} achieved: {self.total_wins}. That is {percentage_of_wins}%.')
        self.clear_total_score()
        self.draw_plots()

    def draw_plots(self):
        fig, axs = plt.subplots(2,3, figsize=(20,10))
        x = self.scores_from_all_challenges['attack'].keys()


        axs[0, 0].bar(x, self.scores_from_all_challenges['attack'].values())
        axs[0, 0].set_title('Attack Challenge')
        axs[0, 1].bar(x, self.scores_from_all_challenges['defense'].values())
        axs[0, 1].set_title('Defense Challenge')
        axs[0, 2].bar(x, self.scores_from_all_challenges['hp'].values())
        axs[0, 2].set_title('Endurance Challenge')
        axs[1, 0].bar(x, self.scores_from_all_challenges['sp_attack'].values())
        axs[1, 0].set_title('Special Attack Challenge')
        axs[1, 1].bar(x, self.scores_from_all_challenges['sp_defense'].values())
        axs[1, 1].set_title('Special Attack Challenge')
        axs[1, 2].bar(x, self.scores_from_all_challenges['speed'].values())
        axs[1, 2].set_title('Speed Challenge')

        fig.suptitle(f'Team {self.team_name} Results')

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


