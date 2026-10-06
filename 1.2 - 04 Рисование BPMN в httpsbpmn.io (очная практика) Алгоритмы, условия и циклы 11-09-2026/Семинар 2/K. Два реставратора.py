# q1, t1, b1 = map(int, input().split())
# q2, t2, b2 = map(int, input().split())

"""
Качество    q — целое от 0 до 100,
время       t — целое от 1 до 600,
допуск      b — 0 или 1.
"""

from random import randint

# q1, t1, b1 = randint(0, 100), randint(1, 600), randint(0, 1)
# q2, t2, b2 = randint(0, 100), randint(1, 600), randint(0, 1)


def robots(q1, t1, b1, q2, t2, b2):

    if q1 == q2:
        if t1 == t2:
            if b1 > b2:
                print('FIRST')
            elif b1 < b2:
                print('SECOND')
            else:
                print('DRAW')
        elif t1 > t2:
            print('SECOND')
        else:
            print('FIRST')
    elif q1 > q2:
        print('FIRST')
    else:
        print('SECOND')

for i in range(100):
    q1, t1, b1 = randint(0, 1), randint(2, 3), randint(4, 5)
    q2, t2, b2 = randint(0, 1), randint(2, 3), randint(4, 5)
    print(f'{q1, t1, b1}\n{q2, t2, b2} ', end='')
    robots(q1, t1, b1, q2, t2, b2)