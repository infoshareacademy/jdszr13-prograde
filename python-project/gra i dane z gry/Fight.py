from Menu import Menu
from PC_Pokemon import PC_Pokemon
from Action_Print import Action_Print
import random
import csv

class Fight:
    '''Class simulating the course of the battle'''


    def __init__(self, path_File, number_Of_Pokemon) -> None:
        self.menu = Menu(number_Of_Pokemon)
        self.menu.choice_Type_Game()
        self.list_Chance_To_Miss = [1, 2, 3, 4, 5]
        # Jeżeli wybór losowy
        for _ in range(number_Of_Pokemon):
            self.menu.choice_Random_Pokemon(path_File)

        # Jeżeli wybór własny   
        self.menu.all_Pokemon(path_File)

        for _ in range(number_Of_Pokemon):
            self.menu.choice_Pokemon(path_File)
            
        self.menu.statistic_Pokemon("Ciebie")
        self.pc_Pokemon = PC_Pokemon(path_File, number_Of_Pokemon)       
      

    def return_User_Pokemon(self) -> str:
        #The function changes the index number from 0 and returns the entire dataframe for the user
        self.menu.df_Pokemon = self.menu.df_Pokemon.reset_index(drop=True)
        print(self.menu.df_Pokemon.index + 1)
        return self.menu.df_Pokemon 


    def return_PC_Pokemon(self) -> str:
        #The function changes the index number from 0 and returns the entire dataframe for the PC
        self.pc_Pokemon.df_Pokemon = self.pc_Pokemon.df_Pokemon.reset_index(drop=True)
        print(self.pc_Pokemon.df_Pokemon.index + 1)
        return self.pc_Pokemon.df_Pokemon 
    

    def battle(self, i : int) -> None:
        '''Combat state simulation function
        We assign life points to Pokemon.
        We check which Pokemon is faster - at the beginning of the battle.
        We check if the difference between attack and defense is positive. If the defense is greater than the attack, we subtract 5 life points each time. Otherwise, we subtract the difference.
        After each hit, the life status and action are printed.
        Finally, the Pokemon that has won is printed.

        
        i - parameter telling which row in the dataframe we refer to
        self.hp_PC - pokemon pc life
        self.hp_User - pokemon user life
        self.chance_To_Miss - draw results with lists, if the result is 1, it will see that stylish missed
        factor_PC - No fighting column, adding factor 1 for this category.
        factor_User - No fighting column, adding factor 1 for this category.
        next_attack - assigning who attacks next


        '''

        action_print = Action_Print()

        next_atack = ""

        print(f"Pokemon PC to: {self.pc_Pokemon.df_Pokemon.loc[i, 'name']} z żciem na poziomie: {self.pc_Pokemon.df_Pokemon.loc[i, 'hp']}")
        print(f"Pokemon Użytkownika to: {self.menu.df_Pokemon.loc[i, 'name']} z żciem na poziomie: {self.menu.df_Pokemon.loc[i, 'hp']}")

        self.hp_PC = self.pc_Pokemon.df_Pokemon.loc[i, 'hp']
        self.hp_User = self.menu.df_Pokemon.loc[i, 'hp']
        self.missing_Attack_PC = 0
        self.missing_Attack_User = 0

        data_List = []
        # print(self.pc_Pokemon.df_Pokemon.loc[i, 'speed'])
        # print(self.menu.df_Pokemon.loc[i, 'speed'])
        # print('\n')
        # print(self.pc_Pokemon.df_Pokemon.loc[i, 'attack'])
        # print(self.menu.df_Pokemon.loc[i, 'attack'])
        # print('\n')
        # print(self.pc_Pokemon.df_Pokemon.loc[i, 'defense'])
        # print(self.menu.df_Pokemon.loc[i, 'defense'])

        if(int(self.pc_Pokemon.df_Pokemon.loc[i, 'speed']) >=  int(self.menu.df_Pokemon.loc[i, 'speed'])):
            next_atack = "pc"
        else:
            next_atack = "user"

        print(f"kolejny ruch: {next_atack}")

        self.column_Names_PC = self.pc_Pokemon.df_Pokemon.columns.tolist()
        self.column_Names_User = self.menu.df_Pokemon.columns.tolist()
        
        factor_PC = 1.0 if(self.menu.df_Pokemon.loc[i, 'type1'] == "fighting") else self.menu.df_Pokemon.loc[i, "against_" + self.menu.df_Pokemon.loc[i, 'type1']]
        factor_User = 1.0 if(self.pc_Pokemon.df_Pokemon.loc[i, 'type1'] == "fighting") else self.pc_Pokemon.df_Pokemon.loc[i, "against_" + self.pc_Pokemon.df_Pokemon.loc[i, 'type1']]

        while(self.hp_PC >= 0 and self.hp_User >= 0):
            self.chance_To_Miss = random.choice(self.list_Chance_To_Miss)
            if(next_atack == "user"):
                action_print.print_Normal_Atack_User(self.menu.df_Pokemon.loc[i, 'name'], self.pc_Pokemon.df_Pokemon.loc[i, 'name'], self.menu.df_Pokemon.loc[i, 'attack'], self.pc_Pokemon.df_Pokemon.loc[i, 'defense'], self.pc_Pokemon.df_Pokemon.loc[i, 'type1'], factor_PC)
                next_atack = "pc"
                if(self.chance_To_Miss != 1):
                    if(self.pc_Pokemon.df_Pokemon.loc[i, 'defense'] - (self.menu.df_Pokemon.loc[i, 'attack'] * factor_PC)>= 0):
                       self.hp_PC = self.hp_PC - 5
                    else:
                        self.hp_PC = self.hp_PC - (self.menu.df_Pokemon.loc[i, 'attack'] * factor_PC) + self.pc_Pokemon.df_Pokemon.loc[i, 'defense']
                else:
                    print("Pudło, nie zadałeś żadnych obrażeń")
                    self.missing_Attack_User += 1
            else:
                action_print.print_Normal_Atack_PC(self.pc_Pokemon.df_Pokemon.loc[i, 'name'], self.menu.df_Pokemon.loc[i, 'name'],  self.pc_Pokemon.df_Pokemon.loc[i, 'attack'], self.menu.df_Pokemon.loc[i, 'defense'], self.menu.df_Pokemon.loc[i, 'type1'], factor_User)
                next_atack = "user"
                if(self.chance_To_Miss != 1):
                    if(self.menu.df_Pokemon.loc[i, 'defense'] - (self.pc_Pokemon.df_Pokemon.loc[i, 'attack'] *  factor_User) >= 0):
                        self.hp_User = self.hp_User - 5
                    else:
                        self.hp_User = self.hp_User - (self.pc_Pokemon.df_Pokemon.loc[i, 'attack'] *  factor_User) + self.menu.df_Pokemon.loc[i, 'defense']
                else:
                    print("Pudło, PC nie zadał żadnych obrażeń")
                    self.missing_Attack_PC += 1

            print(f"Zycie PC {self.pc_Pokemon.df_Pokemon.loc[i, 'name']} to {self.hp_PC}")
            print(f"Zycie User {self.menu.df_Pokemon.loc[i, 'name']} to {self.hp_User}")
            print(f"kolejny ruch: {next_atack}")

        if(next_atack != "pc"):
            print(f"Wygrał PC z pokemonem {self.pc_Pokemon.df_Pokemon.loc[i, 'name']}")
            print(f"Pokemon, który wygrał {self.pc_Pokemon.df_Pokemon.loc[i, 'name']}, wlaczył z {self.menu.df_Pokemon.loc[i, 'name']}, zostało mu życia {self.hp_PC}, współczynnik mocy do przeciwnika {factor_PC}, tyle pudeł zanotował {self.missing_Attack_PC}")
            data = [str(self.pc_Pokemon.df_Pokemon.loc[i, 'name']) , str(self.menu.df_Pokemon.loc[i, 'name']) , str(self.hp_PC) , str(factor_PC), str(self.missing_Attack_PC), self.pc_Pokemon.df_Pokemon.loc[i, 'type1'], self.menu.df_Pokemon.loc[i, 'type1']]
        else:
            print(f"Wygrał User z pokemonem {self.menu.df_Pokemon.loc[i, 'name']}")
            print(f"Pokemon, który wygrał {self.menu.df_Pokemon.loc[i, 'name']}, wlaczył z {self.pc_Pokemon.df_Pokemon.loc[i, 'name']}, zostało mu życia {self.hp_User}, współczynnik mocy do przeciwnika {factor_User}, tyle pudeł zanotował {self.missing_Attack_User}")
            data = [str(self.menu.df_Pokemon.loc[i, 'name']) , str(self.pc_Pokemon.df_Pokemon.loc[i, 'name']) , str(self.hp_User) , str(factor_User) , str(self.missing_Attack_User), self.menu.df_Pokemon.loc[i, 'type1'], self.pc_Pokemon.df_Pokemon.loc[i, 'type1']]

        data_List.append(data)

        csv_file_path = "dane.csv"

        with open(csv_file_path, mode="a", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            #csv_writer.writerow(["Name PC", "Name Menu", "HP PC", "Factor PC", "Missing Attack PC"])  # Nagłówki
            csv_writer.writerows(data_List)

        print("Dane zapisane do pliku CSV.")

        #self.hp_PC = self.pc_Pokemon.df_Pokemon.loc[i, 'hp']
        #self.hp_User = self.menu.df_Pokemon.loc[i, 'hp']
        #factor_User

        print("\n")
        print("\n")
        print("\n")

        