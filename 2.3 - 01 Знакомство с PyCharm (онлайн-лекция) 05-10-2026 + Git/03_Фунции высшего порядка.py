l = [22, 33, 44]

def gen():
    i = 0
    while i < 3:
        i += 1
        yield i


res = gen()

print(res)
print(next(res))
print(next(res))
print(next(res))

for i in res:
    print(i)


for i in res:
    print(i)


# выражение Генератора  - круглые скобки в list comprehension
res = (i for i in gen())
print(list(res))        # [1, 2, 3]
print(list(res))        # []




res = map(str, l)
print(list(res))        # ['22', '33', '44']



def power(n):
    return n * n

res = map(power, l)
print(list(res))        # [484, 1089, 1936]

res1 = (i * i for i in l)





res = map(lambda n: n * n, l)
print(list(res))            # [484, 1089, 1936]


l1 = [1, 2, 3]

res = map(lambda n, m: n - m, l, l1)
print(list(res))            # [21, 31, 41]


res = filter(lambda n: n % 2 == 0, l)
print(list(res))            # [22, 44]

from functools import reduce

city = ('У', 'ф', 'а', '-', 4, 5)
# c = "".join(city)
# print(c)            # TypeError: sequence item 4: expected str instance, int found

def prim(x, y):
    print(x, y)
    print(str(x) + str(y))
    return str(x) + str(y)

res = reduce(prim, city)
print(res)      # Уфа-45




res = reduce(lambda x, y: str(x) + str(y), city)
print(res)      # Уфа-45

res = reduce(lambda x, y: str(y) + str(x), city)
print(res)      # 54-афУ


print(sum(l))
l = range(1, 6)
res = reduce(lambda x, y: x + y, l)
print(res)      # 15


res = reduce(lambda x, y: x * y, l)
print(res)      # 120           - факториал