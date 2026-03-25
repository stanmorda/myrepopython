x = int(input())

# 2347289
# 1) проверять наличие цифр в записи
# 2) смотреть окончание числа
# 3) подсчитывать кол-во определенных цифр в числе

# 1414141 
# 1001
# 101
# 11
# 5555

# 12349 -> 94321

1234
result = 0
k = len(str(x))
numbers = []

while x>0:
    t = x%10
    x = x//10
    result += t*10**(k-1)
    k-=1
    
print(result)


exit(0)

while True:
    x = int(input())
    # 2347289 - 7?

    i = 0
    while x > 9:
        i += 1
        if x % 10 == 7:
            print('YES')
            break
        else:
            x = x // 10    
            print(x)    

    x = str(x)
    i = x.find('7')
    
    if '7' in x:
        print('YES')
    
    # 1.
    # if x % 10 == 9:
    #     print('YES')
    # else:
    #     print('NO')
    
    # 2.
    # x = str(x)
    # if x[-1] == '9':
    #     print('YES')
    # else:
    #     print('NO')