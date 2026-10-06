from tkinter import *

a = 128512

def increment():
    global a
    a += 1
    metka['text'] = chr(a)

def decrement():
    global a
    a -= 1
    metka['text'] = chr(a)

window = Tk()
metka = Label(text=chr(a), fg='DimGray', bg='BlanchedAlmond', width=10, height=3, font='Arial 64 bold')
metka.pack()

knopka = Button(text='Следующий смайл', width=30, height=3, font='Arial 14 bold')
knopka.config(command=increment)
knopka.pack()

knopka = Button(text='Предыдущий смайл', width=30, height=3, font='Arial 14 bold')
knopka.config(command=decrement)
knopka.pack()


window.mainloop()