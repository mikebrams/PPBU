from tkinter import *


def show():
    """Меняет цвет букв"""
    cb1.config(fg=v.get())
    m.config(text=v.get())
    m.config(fg=v.get())


root = Tk()
root.geometry('420x150+600+400')


v = StringVar()
v.set('black')


cb1 = Checkbutton(text='Это переключатель цвета', variable=v, onvalue='red', offvalue='black', command=show)
cb1.pack()

m = Label(text='Метка', width=15, height=3, bg='lightgrey')
m.pack()




root.mainloop()