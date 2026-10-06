k, i, *z = 1, 2, 3, 4, 5, 6, 7

print(k, i, z)


num = [1, 2, 3, 4]
for i in enumerate(num):
    print(i[0], i[1])

names = ['a', 'b', 'c', 'd']

for i in zip(names, num):
    print(i)


num2 = [5, 6, 7, 8]

for x, y in zip(num, num2):
    print(x + y)


for x, y, z in zip(num, num2, names):
    print(str(x) + str(y) + z)

"""
левый циклический сдвиг
"""

l = [22, 33, 44, 55, 99]
temp = l[0]

for i in range(len(l) - 1):
    l[i] = l[i + 1]
l[-1] = temp
print(l)




age = [22, 33, 44, 55, 99]
for r, (n, a) in enumerate(zip(names, age), 1):
    print(f'{r}. {n} - {a}')






