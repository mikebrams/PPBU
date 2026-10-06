from tkinter import *
from tkinter import messagebox as mb


def check():
    answer = mb.askyesno(title='Вопрос', message='Передать данные?')
    if answer:
        s = e.get()
        e.delete(0, END)
        m.config(text=s)


root = Tk()
e = Entry()
e.pack()

b = Button(text='Передать?', command=check)
b.pack()

m = Label(height=3)
m.pack()


root.mainloop()