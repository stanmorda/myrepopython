import pandas as pd

df = pd.read_csv('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок1102/top_100_players.csv')
#1. Вывести список уникальных регионов
# print(df['Region'].unique())

#2. Узнать, из какого региона больше всего игроков
x1 = (
    df
    .groupby('Region')['Name']
    .count()
    .sort_values(ascending=False)
    .head(1)
)

# print(x1)

x2 = (
    df
    .groupby('Region')['Name']
    .count()
    .sort_values(ascending=True)
    .head(1)
)
# print(x2)

#3 Выбрать 5 лучших игроков из Северной Америки, вывести только их имена
x3 = (
    df[df['Region'] == 'North America']
    .sort_values('CS Rating', ascending=False)
    .head(5)
    ['Name']
)
# print(x3)

#4 Выбрать худшего игрока из каждого региона
x4 = (
    df
    .sort_values('CS Rating', ascending=True)
    .groupby('Region')
    .tail(1)
    .sort_values('Rank', ascending=True)
)
# print(x4[['Rank','Region']])

#5 Выбрать игрока, с макасимальной разницей побед и поражений
df['diff_wins_loses'] = df['Wins'] - df['Losses']
print((
    df
    .sort_values('diff_wins_loses', ascending=False)
    .head(1)
    [['Name', 'diff_wins_loses']])
    )
df = df.drop(columns='diff_wins_loses')
# print(df.head(5))

#6 Посчитать среднее количетво побед по каждому региону
x6 = (
    df
    .groupby('Region')
    .mean('Wins')
    ['Wins']
)
# print(x6)
