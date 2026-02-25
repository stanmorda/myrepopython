import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок1802/weather_data.csv')

# x1 = (
#     df.sort_values('Temperature_C', ascending=True)
#     .head(1)
# )
# print(x1[['Location', 'Temperature_C']])

# x2 = (
#     df.groupby('Location')
#     .groups
#     .keys()
# )

# print(x2)

# x2 = (
#     df['Location'].unique()
# )

# print(x2)

# x2 = (
#     df
#     .groupby('Location')
#     ['Temperature_C']
#     .mean()
#     .sort_values()
# )
# print(x2)

x3 = (
    df[df['Location'] == 'Philadelphia']
    [['Date_Time', 'Precipitation_mm']]
    .sort_values('Date_Time', ascending=True)
)

x3.plot(x='Date_Time', y='Precipitation_mm', kind='line')
plt.show()

print(x3)