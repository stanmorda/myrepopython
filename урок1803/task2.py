x = 'xxxYYYttooooooooooooooooooooo'
# print('y'*10)
# 1) zip 'x3Y3t2o15'
t = ''
count = 0

# 't'*9

# m1 = ['z', 'a', 'b']
# m2 = [5, 1, 10]
# # zzzzzabbbbbbbbbb
# r = ''
# for i in range(len(m1)):
#     r += m1[i] * m2[i]
# print(r)
russian_alphabet = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 
    'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 
    'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
]
zip = 'а8п3р2л7'
i = 0
result = ''
while i < len(zip) - 1:
    symbol = zip[i]
    k = i
    
    while zip[i+1] not in russian_alphabet and i+1 < len(zip)-1:
        i += 1
        
    if i+1 == len(zip)-1:
        i += 1
        
    count = int(zip[k+1:i+1])
    result += symbol*count
    i += 1
    
print(result)
# zip[i] - symbol
# zip[i+1] - count



# [x, Y, t]
# [3, 3, 2]

# 2) unzip 'xxxYYYttooooooooooooooooo'


# from random import*
# print(randint(1, 2))