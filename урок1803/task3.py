x = 'i love you very mauuuuuch'
m = x.split(' ')
y = 0
w = ''
for item in m:
    if len(item) > y:
        y = len(item)
        w = item
print(w)