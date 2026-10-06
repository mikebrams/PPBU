from tkinter import *

def change():
    l['text'] = 'Готов к расчётам!'

window = Tk()
window.title('Мой калькулятор')
window.geometry("420x320")

l = Label(text='Привет!')
l.pack()

b = Button(text='Начать', command=change)
b.pack()


window.mainloop()