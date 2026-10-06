num = int(input())
letters = 'ABCEHKMOPTXY'

for _ in range(num):
    code = input()

    a = code[0] in letters
    b = code[1:4].isdigit()
    c = code[4] in letters
    d = code[5] in letters

    e = a + b + c + d

    if len(code) != 6:
        print('No')
    elif e == 4:
        print('Yes')
    else:
        print('No')

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

