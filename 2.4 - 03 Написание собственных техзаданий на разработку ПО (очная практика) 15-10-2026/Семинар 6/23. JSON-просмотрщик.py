"""
json.dumps()	Преобразует объект Python в JSON-строку	json.dumps({"name": "Alice", "age": 30})
json.loads()	Преобразует JSON-строку в объект Python	data = json.loads('{"name": "Bob", "is_student": false}')

json.dump()	    Записывает объект Python в файл в формате JSON	with open("user.json", "w") as f: json.dump({"id": 1}, f)
json.load()	    Читает JSON-файл и возвращает объект Python	with open("user.json") as f: user = json.load(f)
"""

from tkinter import *
import json

def show_field():

    text = note.get('1.0', 'end-1c')

    try:
        data = json.loads(text)
        request = field.get()
        if not request:
            result.config(text='Введите имя поля')
        else:
            try:
                answer = data[request]
                result.config(text=f'{request} = {answer}')
            except KeyError:
                result.config(text=f'Поля нет: {request}')

    except json.JSONDecodeError:
        result.config(text='JSON повреждён')

root = Tk()
root.title('JSON-просмотрщик')
root.geometry('480x360')


note = Text(height=10, width=55)
note.pack(pady=5)

Label(text='Поле:').pack()

field = Entry()
field.pack()

b1 = Button(text='Показать', command=show_field).pack(pady=5)

result = Label(text='Вставьте ответ сервера')
result.pack()

root.mainloop()
