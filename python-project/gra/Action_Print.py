class Action_Print:
    '''Class prints the course of the fight.'''


    def __init__(self) -> None:
        print("Walka się rozpoczęła")


    def print_Normal_Atack_User(self, user_Pokemon : str, pc_Pokemon : str, atack_User_Pokemon : int, defense_User : int, type_Defender_Pokemon : str, attack_Factor : str) -> None:
        #Function to print user pokemon attack on PC pokemon. It also shows attack and defense and how much damage is done
        print(f"Pokemon {user_Pokemon} zaatakował {pc_Pokemon} o ataku {atack_User_Pokemon}, natomiast pokemon użytkownika ma obronę na poziomie {defense_User}. Typ pokemona broniącego się to {type_Defender_Pokemon}, a współczynnik ataku to {attack_Factor}. Użytkownik stracił {atack_User_Pokemon*attack_Factor - defense_User} punktów życia")


    def print_Normal_Atack_PC(self,  pc_Pokemon : str, user_Pokemon : str, atack_Pc_Pokemon : int, defense_User : int, type_Defender_Pokemon : str, attack_Factor : str) -> None:
        #Function to print PC pokemon attack on user pokemon. It also shows attack and defense and how much damage is done
        print(f"Pokemon {pc_Pokemon} zaatakował {user_Pokemon} o ataku {atack_Pc_Pokemon}, natomiast pokemon użytkownika ma obronę na poziomie {defense_User}. Typ pokemona broniącego się to {type_Defender_Pokemon}, a współczynnik ataku to {attack_Factor}. Użytkownik stracił {atack_Pc_Pokemon*attack_Factor - defense_User} punktów życia")

    
    def print_Special_Atack_User(self, user_Pokemon : str, pc_Pokemon : str, atack_User_Pokemon : int, special_Atack : str) -> None:
        #unused
        print(f"Pokemon {user_Pokemon} zaatakował atakiem specjalnym {special_Atack} pokemona {pc_Pokemon} i zabrał {atack_User_Pokemon} punktów życia")


    def print_Special_Atack_PC(self, user_Pokemon : str, pc_Pokemon : str, atack_Pc_Pokemon : int, special_Atack : str) -> None:
        #unused
        print(f"Pokemon {pc_Pokemon} zaatakował atakiem specjalnym {special_Atack} pokemona {user_Pokemon} i zabrał {atack_Pc_Pokemon} punktów życia")
