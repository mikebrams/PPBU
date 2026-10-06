from tkinter import *
import tkinterweb

def read():
    site = e.get()
    frame.load_website(site)

window = Tk()

f1 = Frame(window)
f1.pack()

m = Label(f1, text='Введите адрес сайта: ')
m.pack(side=LEFT)

e = Entry(f1, width=20)
e.pack(side=LEFT)

b = Button(f1, text='Ввод', command=read)
b.pack(side=LEFT)

frame = tkinterweb.HtmlFrame(window)
frame.pack(fill='both',
           expand=1)


window.mainloop()