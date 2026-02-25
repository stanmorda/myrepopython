import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок1802/cleaned_star_data.csv')
# print(df.head(1))


# x2 = (
#     df['Star color'].unique()
# )

# print(x2)

# x3 = (
#     df.groupby('Star color')
#     ['Radius(R/Ro)']
#     .min()
#     .sort_values()
# )
# print(x3)

# all red stars with T>2000

# print(df[(df['mobile'] > 10) & (df['mobile'] < 15)])

# x4 = (
#     df[(df['Star color']=='Red') & (df['Temperature (K)']>2000)]
# )
# print(x4)

x4 = (
    df[(df['Spectral Class']=='B') 
       & (df['Radius(R/Ro)']>0) 
       & (df['Radius(R/Ro)']<1)
       ]
    .sort_values('Temperature (K)', ascending=False)
)
print(x4.head(1)['Temperature (K)'])

df[['Temperature (K)']].plot.hist(alpha=0.5, bins=20)
df[['Radius(R/Ro)']].plot.hist(alpha=0.5, bins=20)
plt.show()