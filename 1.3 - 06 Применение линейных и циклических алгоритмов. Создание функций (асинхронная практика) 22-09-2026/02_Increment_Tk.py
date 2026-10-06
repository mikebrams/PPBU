from tkinter import *

a = 1

def change():
    global a
    a += 1
    metka['text'] = a

window = Tk()
metka = Label(text='1', fg='DimGray', bg='BlanchedAlmond', width=30, height=3, font='Arial 14 bold')
metka.pack()

knopka = Button(text='Увеличение', width=30, height=3, font='Arial 14 bold')
knopka.config(command=change)
knopka.pack()

window.mainloop()