"""
json.dumps()	Преобразует объект Python в JSON-строку	json.dumps({"name": "Alice", "age": 30})
json.loads()	Преобразует JSON-строку в объект Python	data = json.loads('{"name": "Bob", "is_student": false}')

json.dump()	    Записывает объект Python в файл в формате JSON	with open("user.json", "w") as f: json.dump({"id": 1}, f)
json.load()	    Читает JSON-файл и возвращает объект Python	with open("user.json") as f: user = json.load(f)
"""

import json

text = input()
data = json.loads(text)

if data['status'] == 'success':
    breed = data['message'].split('/')[4]
    print(f'Порода: {breed}')
else:
    print(f'Ошибка: {data['message']}')
