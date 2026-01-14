import os

# класс для хранения информации о валюте
class Currency:
    def __init__(self, date, code, minValue, maxValue):
        self.date = date
        self.code = code
        self.minValue = minValue
        self.maxValue = maxValue
        
        
    def delta(self):
        return self.maxValue - self.minValue
        
    def printInfo(self):
        print(self.date, self.code, self.minValue, self.maxValue)
    

my_path = 'C:/Users/momentizm/Documents/Среда.Питон/урок1911/курсы-валют/'
currencies = []
contents = os.listdir(my_path)

# начало обработки файлов
for fileName in contents:
    with open(my_path + fileName, 'r') as file:
        content = file.read().split('\n')
        if len(content) > 3:
            currency = Currency(content[0], content[1], float(content[2]), float(content[3]))
            currencies.append(currency)
            currency.printInfo()
        else:
            print('Невалидный файл:', fileName)
# конец обработки файлов

maxDelta = 0
maxDeltaDay = ''
for item in currencies:
    delta = item.delta()
    if maxDelta < delta:
        maxDeltaDay = item.date
        maxDelta = delta
        
# - сколько файлов обработано
# - минимальная разница в курсах
# - только для EUR
        
print('Максимальная разница курсов=', maxDelta, '. Была:', maxDeltaDay)

