num = int(input())

def func(code):
    letters = 'ABCEHKMOPTXY'

    a = code[0] in letters
    b = code[1:4].isdigit()
    c = code[-2] in letters
    d = code[-1] in letters

    return a + b + c + d

for _ in range(num):
    code = input()

    if func(code) == 4:
        print('YES')
    else:
        print('NO')

"""
5
A123BC
X007MP
K999TY
A12BC3
Z123BC
1
1
1
1
1
"""

