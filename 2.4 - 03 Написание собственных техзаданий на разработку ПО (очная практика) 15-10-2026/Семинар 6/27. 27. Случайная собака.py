import json
from tkinter import *
import requests


def random_dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    # {'message': 'https://images.dog.ceo/breeds/brabancon/n02112706_396.jpg', 'status': 'success'}
    breed = data['message'].split('/')[4]
    l.config(text=f'Порода: {breed}')


root = Tk()
root.title('Пёсики')
root.geometry('360x220')

Button(text='Случайная собака', command=random_dog).pack()
l = Label(text='Нажмите кнопку')
l.pack()

root.mainloop()
