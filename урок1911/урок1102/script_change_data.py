import pandas as pd
import random

df1 = pd.read_csv('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок1102/top_100_players_1.csv')
df2 = pd.read_csv('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок1102/top_100_players_2.csv')

print(df2.head(1))

for index, row in df2.iterrows():
    df2.iloc[index, 4] = random.randint(0, 250)
    df2.iloc[index, 5] = random.randint(0, 20)
    df2.iloc[index, 6] = random.randint(0, 250)
    
df2.to_csv('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок1102/top_100_players_2.csv')