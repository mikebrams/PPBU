from tkinter import *

a = 0
b = 0
c = 0

def add():
    global a
    global b
    global c
    res = int(e1.get()) + int(e2.get()) + int(e3.get())
    print(res)

def multiply():
    global a
    global b
    global c
    res = int(e1.get()) * int(e2.get()) * int(e3.get())
    print(res)

window = Tk()
window.title('Калькулятор')

window.geometry('400x250+400+300')       # widthxheight+x+y.



zagolovok = Label(text='Введите три числа и нажмите на кнопку для вычисления суммы', height=3)
zagolovok.pack()

e1 = Entry()
e1.pack()

e2 = Entry()
e2.pack()

e3 = Entry()
e3.pack()

b1 = Button(text='Сложить три числа', command=add)
b1.pack()

b2 = Button(text='Умножить три числа', command=multiply)
b2.pack()




window.mainloop()
