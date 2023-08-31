import pandas as pd
from Fight import Fight


number_Of_Pokemon = 6 #defulte 6 pokemon

fight = Fight("pokemon.csv", number_Of_Pokemon)
df_user = fight.return_User_Pokemon()
df_PC = fight.return_PC_Pokemon()

print(df_user)
print(df_PC)


for i in range(number_Of_Pokemon):
    fight.battle(i)

