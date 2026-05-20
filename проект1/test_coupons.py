import pandas as pd

df = pd.read_csv('C:/Users/momentizm/Documents/1map-winners.csv', sep=';')

# 1. Очищаем суммы от пробелов и превращаем в числа
df['Сумма'] = df['Сумма'].astype(str).str.replace(' ', '').astype(float)
df['Коэф.'] = df['Коэф.'].astype(str).str.replace(',', '.').astype(float)
df['Выплата'] = df['Сумма'] * df['Коэф.']

# 1. Сначала отфильтруем нужный счет
df_filtered = df[df['Счёт'] == '16:20']


# 4. Группируем по 'Ставка' и считаем разные метрики
result = df_filtered.groupby('Ставка').agg(
    Общая_Сумма=('Сумма', 'sum'),
    Общая_Выплата=('Выплата', 'sum'),
    Средний_Коэф=('Коэф.', 'mean'),
    Кол_во_Ставок=('Ставка', 'count')
).reset_index()

print(result)