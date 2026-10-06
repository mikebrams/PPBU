from tkinter import *

a = 0

def change():
    global a
    a += 1
    l['text'] = f'Нажатий: {a}'

window = Tk()
window.title('Мой калькулятор')
window.geometry("420x320")

l = Label(text='Нажатий: 0')
l.pack()

b = Button(text='Проверить', command=change)
b.pack()


window.mainloop()