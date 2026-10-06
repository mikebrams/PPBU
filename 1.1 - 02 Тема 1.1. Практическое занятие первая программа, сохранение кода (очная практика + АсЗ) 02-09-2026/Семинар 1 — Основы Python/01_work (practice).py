# num = int(input())
#
# t = num // 1000
# s = num % 1000 // 100
# d = num % 1000 % 100 // 10
# e = num % 10
#
# print(f'Тысячи: {t}')
# print(f'Сотни: {s}')
# print(f'Десятки: {d}')
# print(f'Единицы: {e}')
# print(f'Сумма цифр: {t + s + d + e}')
# print(f'Произведение цифр: {t * s * d * e}')
# print(f'Обратный код: {e}{d}{s}{t}')
from calendar import firstweekday
from math import floor

# f = int(input())
# s = int(input())
# t = int(input())
#
# fp = int(f // 2 + f % 2)
# sp = int(s // 2 + s % 2)
# tp = int(t // 2 + t % 2)
#
#
# print(f'Первый класс: {fp}')
# print(f'Второй класс: {sp}')
# print(f'Третий класс: {tp}')
# print(f'Всего парт: {fp + sp + tp}')
#


# n = int(input())
# match n:
#     case n if n < -20: print('Режим: ЭКСТРЕМАЛЬНЫЙ ХОЛОД')
#     case n if -20 <= n < 0: print('Режим: ХОЛОДНО')
#     case n if 0 <= n < 20: print('Режим: ПРОХЛАДНО')
#     case n if 20 <= n < 30: print('Режим: КОМФОРТНО')
#     case _: print('Режим: ЖАРКО')

# g1 = int(input())
# g2 = int(input())
# g3 = int(input())
#
# max_power = max(g1, g2, g3)
# leaders = 0
#
# if max_power == g1:
#     leaders += 1
# if max_power == g2:
#     leaders += 1
# if max_power == g3:
#     leaders += 1

# a = int(input())
#
# match a:
#     case a if a < 0: print('Положение: СЛЕВА')
#     case a if a > 0: print('Положение: СПРАВА')
#     case _: print('Положение: В БАЗЕ')

# flat = int(input())     # номер квартиры
# k = int(input())        # кол-во квартир на этаже
#
# flor = flat // k + (1 if flat % k else 0)    # этаж
# pos = flat % k + (k if not flat % k else 0)     # позиция на этаже
#
# print(f'Этаж: {flor}')
# print(f'Позиция на этаже: {pos}')

# print(4 % 3)
# print(5 % 4)
# print(3 // 4)
# print(3 // 4)
# print(3 // 4)
# print(3 // 4)
# print(3 // 4)
# print(3 // 4)
# print(1 % 4)
# print(2 % 4)
# print(3 % 4)
# print(4 % 4)
#
#
# print(1 // 4)
# print(2 // 4)
# print(3 // 4)
# print(4 // 4)

# print(a := int(input()), 'СЛЕВА' if a < 0 else 'СПРАВА')
#
# print(f'Максимальная мощность: {max_power}')
# print(f'Количество лидеров: {leaders}')



# if a + b <= c or b + c <= a or c + a <= b:
#     print('Режим: ТРЕУГОЛЬНИК НЕ СУЩЕСТВУЕТ')
# elif a == b and b == c and c == a:
#     print('Режим: РАВНОСТОРОННИЙ')
# elif a != b and b != c and c != a:
#     print('Режим: РАЗНОСТОРОННИЙ')
# else:
#     print('Режим: РАВНОБЕДРЕННЫЙ ')




# if not n % 400 or not n % 4 and n % 100:
#     print('Год: ВИСОКОСНЫЙ')
# else:
#     print('Год: НЕВИСОКОСНЫЙ')



# if x > 0 and y > 0:
#     print('Положение: ПЕРВАЯ ЧЕТВЕРТЬ')
# elif x < 0 and y > 0:
#     print('Положение: ВТОРАЯ ЧЕТВЕРТЬ')
# elif x < 0 and y < 0:
#     print('Положение: ТРЕТЬЯ ЧЕТВЕРТЬ')
# elif x > 0 and y < 0:
#     print('Положение: ЧЕТВЁРТАЯ ЧЕТВЕРТЬ')
# elif x == 0 and y != 0:
#     print('Положение: ОСЬ Y')
# elif y == 0 and x != 0:
#     print('Положение: ОСЬ X')
# else:
#     print('Положение: НАЧАЛО КООРДИНАТ')


# print(f'Сигнал: {'НЕЧЁТНЫЙ' if int(input()) % 2 else 'ЧЁТНЫЙ'}')



a = '01010101 10001001 11100101 11101000 11111100 11111111 11111111 11111111 10000011 11111000 01000001 01110101 00001101 01101000 00000000 00000000 00000000 11101000 11111100 11111111 11111111 10000011 11000100 00000100 10111000 00000000 00000000 00000000 10001001 11101100 01011101 11000011'


# fio = input("Введите ФИО: ")
#
# print(fio.replace(" ","\n"))

a = [1, 2, 3]
b = [4, 5, 6]


print(zip(a, b))




