import math

result = {}


for i in open('ice-cream.csv', 'r', encoding='utf-8'):
    ls = i.strip().split(';')
    for topping in set(ls):
        if topping.startswith('t'):
            continue
        elif topping not in result:
            result[topping] = 1
        else:
            result[topping] += 1

mx = 0
name_max = ''

mn = math.inf
name_min = ''

for topping, count in result.items():
    if count > mx:
        mx = count
        name_max = topping
    if count < mn:
        mn = count
        name_min = topping

print(result)
print(name_max)
print(name_min)
