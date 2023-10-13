import pandas as pd
from Menu import Menu

class PC_Pokemon(Menu):
    '''Class that selects pokemons for the computer'''


    def __init__(self, path_File : str, number_Of_Pokemon : int) -> None:
        self.choic_Randomly = False
        self.choic = True
        self.df_Pokemon = pd.DataFrame(columns=['name', 'type1', 'hp', 'attack'])

        for _ in range(number_Of_Pokemon):
            self.choice_Random_Pokemon(path_File)

        print("Pokemony przeciwnika")
        self.statistic_Pokemon("PC")