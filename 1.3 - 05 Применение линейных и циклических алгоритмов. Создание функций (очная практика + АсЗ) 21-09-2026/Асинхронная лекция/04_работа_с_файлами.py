with open('D:\\Projects\\OsnovaniePy2026\\Задание 2 - до 28.09.2026\\calculations.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

print(lines)        # ['Результат: 1 + 1 = 2\n', 'Результат: 1 + 2 = 3\n']


with open('D:\\Projects\\OsnovaniePy2026\\Задание 2 - до 28.09.2026\\calculations.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line, end='')
# Результат: 1 + 1 = 2
# Результат: 1 + 2 = 3


with open('D:\\Projects\\OsnovaniePy2026\\Задание 2 - до 28.09.2026\\calculations.txt', 'r', encoding='utf-8') as file:
    line = file.readline()
    print(line, end='')             # Результат: 1 + 1 = 2
    line = file.readline()
    print(line, end='')             # Результат: 1 + 1 = 2

with open('example.txt', 'w', encoding='utf-8') as file:
    file.write('Привет, мир!\n')
    file.write('Это пример записи в файл.\n')

lines = ['Строка 1\n', 'Строка 2\n', 'Строка 3\n']
with open('example.txt', 'a', encoding='utf-8') as file:
    file.writelines(lines)


with open('example.txt', 'a', encoding='utf-8') as f:
    print('Привет, мир!', file=f)       # для вывода форматированных строк
