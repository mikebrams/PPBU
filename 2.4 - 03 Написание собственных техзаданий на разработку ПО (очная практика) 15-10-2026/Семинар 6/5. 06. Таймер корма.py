text = input()

try:
    n = int(text)
    print(f'Таймер: {n} мин')
except ValueError:
    print("Это не число")
