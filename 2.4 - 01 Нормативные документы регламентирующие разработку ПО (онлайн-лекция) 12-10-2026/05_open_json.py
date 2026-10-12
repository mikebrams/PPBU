import json
from idlelib.debugobj import ObjectTreeItem

# d = {'black': 'черный',
#      'white': 'белый'}

# with open('dict.json', 'w', encoding='utf-8') as file:
#     json.dump(d, file, indent=4)        # indent - для переноса данных на новую строку

with open('dict.json', 'r', encoding='utf-8') as file:
    d = json.load(file)


while True:
    word = input('Введите слово для перевода: ')

    if word in d:
        print(f'{word} - {d[word]}')
    elif word == 'exit':
        break
    else:
        translate = input(f'Введите перевод слова "{word}": ')
        d[word] = translate

    with open('dict.json', 'w', encoding='utf-8') as file:
        json.dump(d, file, indent=4)




print(d)