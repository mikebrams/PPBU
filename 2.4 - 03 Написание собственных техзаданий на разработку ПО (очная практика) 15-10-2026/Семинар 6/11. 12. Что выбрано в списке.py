breeds = input().split(", ")
line = input()
selection = () if line == "" else (int(line),)

if not selection:
    print('Сначала выберите породу')
else:
    print(f'Выбрано: {breeds[selection[0]]}')