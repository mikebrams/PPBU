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



