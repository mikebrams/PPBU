name = input()
n = name.strip()
n_len = len(n)

if not n:
    print('Ошибка: пустое имя')
elif n_len > 12:
    print('Ошибка: слишком длинное имя')
elif sum([l.isdigit() for l in n]):
    print('Ошибка: в имени цифры')
else:
    print(f'Имя принято: {n}')

