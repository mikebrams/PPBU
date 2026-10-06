num = int(input())

letters = 'ABCEHKMOPTXY'

# output = []

for i in range(num):
    code = input()

    if len(code) != 6:
        # output.append('No')
        print('No')
    elif code[0] in letters and code[1:4].isdigit() and \
            code[-2] in letters and code[-1] in letters:
        # output.append('Yes')
        print('Yes')
    else:
        # output.append('No')
        print('No')

# for i in range(len(output)):
#     print(output[i])



# print(*output, sep='\n')

# codes_list = []
#
# for i in range(num):
#     code_a = input()
#     codes_list.append(code_a)
#
# for i in codes_list:
#
#     if len(i) != 6:
#         print('NO')
#     elif i[0] in letters and i[1:4].isdigit() and \
#             i[-2] in letters and i[-1] in letters:
#         print('YES')
#     else:
#         print('NO')

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

