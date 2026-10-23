text = input()

if len(text) != 5 or text[2] != ':':
    print('Такого времени нет')
elif not int(text[0:2]) <= 23 or not int(text[3:]) <= 59:
    print('Такого времени нет')
else:
    print('Время есть')
