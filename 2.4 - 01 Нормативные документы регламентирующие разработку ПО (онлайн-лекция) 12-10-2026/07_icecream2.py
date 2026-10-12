import math

result = {}

for i in open('ice-cream.csv', 'r', encoding='utf-8'):
    ls = i.strip().split(';')
    for topping in set(ls):
        if topping.startswith('t'):
            continue
        result[topping] = result.get(topping, 0) + 1

        # elif topping not in result:
        #     result[topping] = 1
        # else:
        #     result[topping] += 1

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


mx = max(result.items(), key=lambda x: x[1])[0]
mx2 = sorted(result.items(), key=lambda x: -x[1])
mn = min(result.items(), key=lambda x: x[1])[0]
mn2 = sorted(result.items(), key=lambda x: x[1])

print(result)
print(name_max)
print(name_min)

print(mx)
print(mn)
print(mx2)
print(mn2)
