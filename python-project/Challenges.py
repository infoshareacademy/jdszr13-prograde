import matplotlib.pyplot as plt
import random

class Challenges:
    '''
        Class that creates challenges for given pokemon teams

        |player_team            pandas dataframe with player chosen pokemons
        |team_name              string with team's name
        |possible_opponents     pandas dataframe with opponent pokemons
    '''

    def __init__(self, player_team:str, team_name, possible_opponents):
        self.player_team = player_team.reset_index()
        self.team_name = team_name
        self.possible_opponents = possible_opponents
        self.pokemon_score = {}
        self.scores_from_all_challenges = {'attack': {},'defense':{}, 'hp':{}, 'sp_attack':{}, 'sp_defense':{}, 'speed':{}}
        self.current_challenge_wins = 0
        self.total_wins = 0
        self.challenge_types = ['attack', 'defense', 'hp', 'sp_attack', 'sp_defense', 'speed']

    def choose_random_opponent(self):
        random.seed(10)
        return self.possible_opponents.sample(1) 
    
    def create_pokemon_individual_score_table(self):
        self.pokemon_score = {}
        for i in range(len(self.player_team)):
            self.pokemon_score[self.player_team['name'].iloc[i]] = 0

    def clear_score(self):

        self.total_wins = 0

    def increase_current_score(self):
        self.current_challenge_wins += 1
    
    def clear_total_score(self):
        self.pokemon_score = {}
        self.scores_from_all_challenges = {'attack': {},'defense':{}, 'hp':{}, 'sp_attack':{}, 'sp_defense':{}, 'speed':{}}
        self.current_challenge_wins = 0
        self.total_wins = 0
        self.challenge_types = ['attack', 'defense', 'hp', 'sp_attack', 'sp_defense', 'speed']
    
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
            self.scores_from_all_challenges[challenge_type].update(score[1]) 
        
        print(self.scores_from_all_challenges)
        percentage_of_wins = int(self.total_wins/3600*100)
        print(f'Out of possible 3600 wins, team {self.team_name} achieved: {self.total_wins}. That is {percentage_of_wins}%.')
        try:
            return self.scores_from_all_challenges
        finally:
            self.clear_total_score()
        


