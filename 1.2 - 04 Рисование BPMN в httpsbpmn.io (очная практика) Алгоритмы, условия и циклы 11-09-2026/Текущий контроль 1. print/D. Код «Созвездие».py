# n = input()
# int_n = int(n)
#
# if len(set(n)) == 1:
#     print('MASTER')
# elif n == n[::-1]:
#     print('MIRROR')
# elif n[1] == str(int(n[0])+1) and n[2] == str(int(n[1])+1) and n[3] == str(int(n[2])+1):
#     print('LADDER')
# elif n[2] == str(int(n[3])+1) and n[1] == str(int(n[2])+1) and n[0] == str(int(n[1])+1):
#     print('LADDER')
# elif n[:2] in ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']:
#     print('TWIN')
# elif n[1:3] in ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']:
#     print('TWIN')
# elif n[2:] in ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']:
#     print('TWIN')
# else:
#     print('REJECT ')

n = input()         # 1234
# int_n = int(n)

"""
MASTER — все четыре цифры одинаковы;
MIRROR — код одинаково читается слева направо и справа налево;
LADDER — каждая следующая цифра ровно на 1 больше предыдущей либо каждая следующая цифра ровно на 1 меньше предыдущей;
TWIN — есть хотя бы одна пара одинаковых соседних цифр;
REJECT — ни одно из предыдущих правил не выполнено.
"""

master =
mirror = ''


while n:

    num = n % 10

    if master != num:
        master = num

    mirror += str(num)

    if




    num //= 10
if len(set(n)) == 1:
    print('MASTER')
elif n == n[::-1]:
    print('MIRROR')
elif n[1] == str(int(n[0])+1) and n[2] == str(int(n[1])+1) and n[3] == str(int(n[2])+1):
    print('LADDER')
elif n[2] == str(int(n[3])+1) and n[1] == str(int(n[2])+1) and n[0] == str(int(n[1])+1):
    print('LADDER')
elif '11' in '00112233445566778899':
    print('TWIN')
# elif n[1:3] in ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']:
#     print('TWIN')
# elif n[2:] in ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']:
#     print('TWIN')
else:
    print('REJECT ')

print('11' in '00112233445566778899')