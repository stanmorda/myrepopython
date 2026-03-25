# numbers = [1, 2, 1, 3, 4, 4, 6, 0, 4, 34]

# numbers.remove(1)

# print(numbers)
# # 4 34


# int(input())


numbers  = ['a','asd', 'a', 'asd', 'asd']
unique = dict()

for x in numbers:
    if x in unique:
        unique[x] = unique[x] + 1
    else:
        unique[x] = 1    

# 'a' -> 2
# 'asd' -> 3


# [1, 2, 4, 5, 6, 7, 8, 9, 10]
# step = 3
# current = 0
# i = 0
# while len(numbers) != 1:
#     counts = 0
#     while counts != step:
#         i += 1
#         if i == len(numbers):
#             i = 0
#         counts += 1
#     print(i)
#     numbers.remove(i)

        
# exit(0)

# [1, 2, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 4, 5, 7, 8, 10]
# [1, 4, 5, 7, 8, 10]
# [1, 4, 5, 8, 10]
# [4, 5, 8, 10]
# [4, 5, 10]
# [4, 10] -> ответ

# x = 3

# [1, N]



# 1 version
for x in numbers:
    if numbers.count(x) == 1:
        print(x)
     
# 2 version

print('-------')
unique = dict()
# unique['yaroslav'] = 14
# unique['misha'] = 90

for x in numbers:
    if x in unique:
        unique[x] = unique[x] + 1
    else:
        unique[x] = 1    

for key in unique.keys():
    if unique[key] == 1:
        print(key)        

print('----')
# 3 version
for x in numbers:
    count = 0
    
    for y in numbers:
        if x == y:
            count += 1
            
    if count == 1:
        print(x)

exit(0)

# 
# [28.02.2026 15:04] Станислав:
# Задание: дана последовательность чисел. 
# Определить , сколько чисел в ней начинаются и заканчиваются на одну и ту же цифру.

# 10001
# 1001
# 101
# 11
# 1

# [04.03.2026 18:16] Станислав: 601, 152, 878, 737
# [04.03.2026 18:16] Станислав: 1
# [04.03.2026 18:16] Станислав: 60, 52, 878, 737
numbers = [601, 152, 878, 737]
# numbers = [601, 152, 878, 737] -> [60, 52, 878, 737]
x = str(1)
for i in range(len(numbers)):
    item = numbers[i]
    item = str(item).replace(x, '')
    numbers[i] = int(item)
print(numbers)
exit(0)
# x == x[::-1]

# t = x[::-1] # reverse string in python 

def reverse(y):
    x = []

    for i in y:
        x.append(i)
        
    for i in range(len(x)//2):
        t = x[i]
        x[i] = x[len(x)-i-1]
        x[len(x)-i-1] = t
        
    return ''.join(x)

# print(x)
# print(reverse(x))
# print(t)


from random import*
numbers = []
for i in range(10):
    numbers.append(randint(0, 1000))
    
print(numbers)
exit(0)
# 1) определить с какой цифры начинается число
# 2) определить на какую цифру заканчивается число

x = 98765
y = x
r = 0

while y > 0:
    y = y // 10
    r += 1
    
end = x % 10
start = x // 10**(r-1)
print(start, end)
exit(0)
# 34539345 => '34539345'

# 3
# 5

x = 601
s = 0
for i in str(x):
    s += int(i) 

# s[0]
# s[len(s)-1]

# три раза встречается цифра 7
count = 0
for n in numbers:

    n = str(n)
    x = n.count('7')
    if x == 3:
        count+=1
        
    # if n[0] == n[len(n)-1]:
    #     print(n)
    #     count += 1
        
print(count)

