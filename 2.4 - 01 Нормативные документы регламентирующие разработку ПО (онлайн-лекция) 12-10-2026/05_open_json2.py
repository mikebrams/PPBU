import json

# d = {'black': 'черный',
#      'white': 'белый'}

# with open('dict.json', 'w', encoding='utf-8') as file:
#     json.dump(d, file, indent=4)        # indent - для переноса данных на новую строку

with open('dict.json', 'r', encoding='utf-8') as file:
    d = json.load(file)

print(d)

# while True:
#     word = input('Введите слово для перевода: ')
#
#     if word in d:
#         print(f'{word} - {d[word]}')
#     elif word == 'exit':
#         break
#     else:
#         translate = input(f'Введите перевод слова "{word}": ')
#         d[word] = translate

# with open('dict2.json', 'w', encoding='utf-8') as file:
b = json.dumps(d, indent=4)

c = json.loads(b)

print(b)
print(c)