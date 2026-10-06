from tkinter import *
import datetime as dt

def date_time():
    m.config(text=f'{date} {time}')
    print(var)

def date_():
    m.config(text=f'{date}')
    print(var)

def time_():
    m.config(text=f'{time}')
    print(var)

def night():
    m.config(bg='black', fg='white')
    r1.config(bg='black', fg='white')
    r2.config(bg='black', fg='white')
    r3.config(bg='black', fg='white')
    r4.config(bg='black', fg='white')
    print(var)


root = Tk()

d = dt.datetime.now()
date = d.strftime('%d %B %Y')
time = d.strftime('%X')

var = IntVar()
var.set(0)


r1 = Radiobutton(text='Дата и время', command=date_time, variable=var, value=0)
r1.pack(side=LEFT)

r2 = Radiobutton(text='Дата', command=date_, variable=var, value=1)
r2.pack(side=LEFT)

r3 = Radiobutton(text='Время', command=time_, variable=var, value=2)
r3.pack(side=LEFT)

r4 = Radiobutton(text='Ночная тема', command=night, variable=var, value=3)
r4.pack(side=LEFT)

m = Label(text=f'{date} {time}', font='Verdana 24 bold')
m.pack(side=LEFT)


root.mainloop()



"""
import tkinter as tk

root = tk.Tk()

# Создаём общую переменную
choice = tk.StringVar()

# Создаём радиокнопки
radio_python = tk.Radiobutton(root, text='Python', variable=choice, value='Py')
radio_java = tk.Radiobutton(root, text='Java', variable=choice, value='Ja')

radio_python.pack()
radio_java.pack()

# При нажатии на кнопку будет выведено текущее значение переменной
def print_choice():
    print("Вы выбрали:", choice.get())

# Можно добавить кнопку для ручного изменения выбора
button_change = tk.Button(root, text="Изменить выбор", command=print_choice)
button_change.pack()

root.mainloop()
"""
