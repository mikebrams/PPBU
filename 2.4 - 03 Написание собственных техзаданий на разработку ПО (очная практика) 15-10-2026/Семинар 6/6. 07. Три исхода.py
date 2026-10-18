text = input()

try:
    n = int(text)
except ValueError:
    print("Это не число")
else:
    if 1 <= n <= 120:
        print(f'Таймер: {n} мин')
    else:
        print('Нужно от 1 до 120 минут')