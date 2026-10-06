"""
Для каждой записи числа определим её сложность C = L + D
L — количество символов в записи числа;
D — количество различных символов, которые встречаются в этой записи.

"""

n = int(input())

def convert(n, base):

    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while n > 0:
        result = digits[n % base] + result  # Добавляем остаток (как индекс) в начало result
        n //= base
    return result or '0'    # Возвращаем '0', если вход был 0


for i, j in enumerate(range(2, 37), 2):
    print(f'{i:2} - {convert(1000000000, j):>4}')  # Выведет '101'

# print(convert(20, 16))

base = ''
num = ''

complexity = 0

for i in range(2, 37):
    res = convert(n, i)
    L = len(res)
    D = len(set(res))
    C = L + D
    if not base:
        base = i
        num = res
        complexity = C
    elif C < complexity:
        base = i
        num = res
        complexity = C

print(base, num, sep='\n')

# print(f'{i} - {convert(n, i)}')



