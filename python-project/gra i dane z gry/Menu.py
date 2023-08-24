import pandas as pd

class Menu():
    '''The class contains functions to print menus in the console and generate dataframe of selected or random pokemons '''


    def __init__(self, number_Of_Pokemon : int) -> None:
        #Game start menu
        self.df = pd.DataFrame() 
        self.df_Pokemon = pd.DataFrame()
        self.number_Of_Pokemon = number_Of_Pokemon
        print("1 -> Nowa gra")
        print("2 -> Wyjście")


    def choice_Type_Game(self) -> None:
        #Pokemon selection menu manually or randomly
        self.choic = True if input() == "1" else False
        print(self.choic)
        if(self.choic):
            print(f"1 -> Wybierz własne {self.number_Of_Pokemon} pokemonów")
            print(f"2 -> Wybierz losowo {self.number_Of_Pokemon} pokemonów")
            self.choic_Randomly = True if input() == "1" else False


    def all_Pokemon(self, path_File : str) -> None:
        #Reading the data file and assigning it to the dataframe
        if(self.choic):
            self.df = pd.read_csv(path_File)
            print(self.df[['name', 'type1', 'hp', 'attack']]) 


    def choice_Pokemon(self, path_File : str) -> None:
        #Function responsible for the selection of pokemons by the user
        if(self.choic_Randomly and self.choic):
            self.df = pd.read_csv(path_File)
            self.choic_Pokemon = input("Wybierz numer pokemona: ")
            self.df_Pokemon = self.df_Pokemon.append(self.df.loc[int(self.choic_Pokemon)], ignore_index=True)


    def choice_Random_Pokemon(self, path_File : str) -> None:
        #Function responsible for the selection of random pokemons
        if(self.choic_Randomly == False and self.choic):
            self.df = pd.read_csv(path_File)
            random_element = self.df.sample()
            self.df_Pokemon = pd.concat([self.df_Pokemon, random_element])


    def statistic_Pokemon(self, person : str) -> None:
        #pokemon list printing function
        if(self.choic):
            print(f"Oto 6 wybranych losowo pokemonów dla {person}: \n")
            print(self.df_Pokemon[['name', 'type1', 'hp', 'attack']])