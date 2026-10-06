def summ(a, b):
    print(a + b)
    return a * b

n = '45'
cc = 'qwerty'

# summ(n, cc)
# summ(5, 7)

print(summ(5, 7))


def summ(a, b=4):
    print(a + b)
    return a * b

n = '45'
cc = 'qwerty'

# summ(n, cc)
# summ(5, 7)

print(summ(5))

def summ(a=10, b=4):
    print(a + b)
    return a * b

n = '45'
cc = 'qwerty'

# summ(n, cc)
# summ(5, 7)

print(summ(b=8))


def printing(*args):
    print(args)
    return sum(args)

print(printing(1, 2, 3))


def abc(*args, **kwargs):
    print(args)
    print(kwargs)


abc(c='d')



a = [1, 2, 3, 4, 5, 7]
b = [1, 2, 3, 4, 5, 6]

dd = {k: v**2 for k, v in zip(a, b)}
print(dd)

abc(dd)

s = ['Буря', 'мглою', 'небо', 'кроет']
i = 0
while i < len(s):
    if s[i] == 'мглою':
        i += 1
        continue
    print(s[i])
    i += 1

