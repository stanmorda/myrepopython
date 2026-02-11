import pandas as pd


df1 = pd.read_csv('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок1102/top_100_players_1.csv')
df2 = pd.read_csv('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок1102/top_100_players_2.csv')


for index, row in df1.iterrows():
    name = row['Name']
    row2 = df2[df2['Name'] == name]
    print(name, row['Wins']-row2['Wins'])

# def find_best_diff(df):
#     #5 Выбрать игрока, с макасимальной разницей побед и поражений
#     df['diff_wins_loses'] = df['Wins'] - df['Losses']
#     print((
#         df
#         .sort_values('diff_wins_loses', ascending=False)
#         .head(1)
#         [['Name', 'diff_wins_loses']])
#         )
#     df = df.drop(columns='diff_wins_loses')

# find_best_diff(df1)
# find_best_diff(df2)