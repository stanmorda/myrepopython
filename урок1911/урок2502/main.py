# переводит число из 10-й системы счисления в 2-ю
def to2(x10):
    if x10 == 0:
        return '0'
    if x10 == 1:
        return '1'
    result = '' # для аккумулирования ответа будем использовать строку
    while x10 > 1:
        r = x10 % 2
        result = str(r) + result
        x10 //= 2
    return '1' + result

def to10(x2):
    # 1010
    result = 0
    x2 = str(x2)
    for i in range(len(x2)):
        symbol = int(x2[i])
        result += symbol*(2**(len(x2)-i-1))
    return result

print(to10(111))
exit(0)
# 0 -> 0
# 1 -> 1
# 51 -> 110011
# 270 -> 100001110

print(to2(0))
print(to2(1))
print(to2(51))
print(to2(270))

# while
# x % 2 - остаток от деления на 2
# x // 2 - целая часть от деления на 2