try:
    file = open('proba.txt', encoding='utf-8')
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print('Файл не найден')


try:
    with open('proba.txt', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('Файл не найден')
