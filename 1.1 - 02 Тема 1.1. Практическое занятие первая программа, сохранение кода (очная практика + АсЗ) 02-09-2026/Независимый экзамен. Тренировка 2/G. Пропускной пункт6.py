num = int(input())

allowed = set("ABCEHKMOPTXY")

for i in range(num):
    code = input()

    if len(code) != 6:
        print('No')
    elif code[0] in allowed and "0" <= code[1] <= "9" and "0" <= code[2] <= "9" and \
          "0" <= code[3] <= "9" and code[-2] in allowed and code[-1] in allowed:
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



print("0" <= '5' <= "9")