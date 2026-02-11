import pandas as pd
import matplotlib.pyplot as plt
import random

# Define a function to double the value
# def random_value(x):
#     return random.randint(10, 250)


# df1 = pd.read_csv('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок0402/Internet Speed 2022.csv')
# df2 = pd.read_csv('copy_data.csv')
# for index, row in df1.iterrows():
#     country = row['country']
#     data1 = row['mobile']
#     row2 = df2[df2['country'] == country]
#     if row2 is not None:
#         data2 = row2['mobile']
#         print(country, data2-data1)

# # Apply the function to column 'A'
# df['mobile'] = df['mobile'].apply(random_value)
# df.to_csv('copy_data.csv')

# df = df.sort_values('mobile', ascending=False)
# df.hist(column='mobile', bins=10)
# plt.show()
# print(df.head(1))
# print(df.loc[[10,20,30]])
# new_country = {
#     'country': 'Галактическая Республика', 
#     'broadband': 1342, 
#     'mobile': 295.45
#     }
# 100 150

# print(df[df['mobile'].between(10, 15)])
# print(df[(df['mobile'] > 10) & (df['mobile'] < 15)])
# print(df[df['country']=='Russia'])

# df = (df['mobile']
#       .sort_values(ascending=False)
#       .iloc[20:30]
#       .agg(['mean']))

# print(df)
# df = df[df['country'].str.len() == 5]
# df = df.sort_values('broadband', ascending=True)
# print(df.tail(1))

# added_df = pd.DataFrame([new_country])
# df = pd.concat([added_df, df], ignore_index=True)
# print(df.head())

# df.drop([0,1,2], inplace=True)
# print(df.head())
# avgBroadcast = df['broadband'].agg(['min'])
# avgMobile = df['mobile'].agg(['min'])
# print(avgMobile)



# df = df.sort_values('mobile', ascending=False)
# # print(df.head())



# city = {
#     'Город': ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург'],
#     'Год основания': [1147, 1703, 1893, 1723], 
#     'CountOfPeople': [11.9, 4.9, 1.5, 1.4]
#         } 

# # Создаём словарь с нужной информацией о городах.
# df = pd.DataFrame(city) # Превращаем словарь в DataFrame, используя стандартный метод библиотеки.

# print(df[df['CountOfPeople'] > 4])

