e = int(input())    # изначально накопленный заряд
t = int(input())    # минимальный заряд для запуска маяка
g = int(input())    # каждый день солнечная панель добавляет 'g' единиц
d = int(input())    # если заряда не достаточно, ночью расходуется 'd' единиц

Flag = True
days = 0

while Flag:

    if e >= t:
        Flag = False

    else:
        e += g
        if e >= t:
            Flag = False
        else:
            e -= d
        days += 1

print(f'{days} {e}')






