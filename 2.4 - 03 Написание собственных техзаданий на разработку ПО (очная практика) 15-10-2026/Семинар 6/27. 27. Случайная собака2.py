from tkinter import *
import requests


def random_dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    #
    # print(type(data))
    # print(response.status_code)
    # print(data['status'])
    #
    # response_text = response.text
    # data2 = json.loads(response_text)
    # print(type(data2))
    # print(data2['status'])
    #
    print(data)

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
