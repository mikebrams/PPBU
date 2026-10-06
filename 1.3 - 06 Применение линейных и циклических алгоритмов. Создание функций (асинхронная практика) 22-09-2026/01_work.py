from tkinter import *

def change():
    metka['text'] = 'Absolutely!'
    metka['bg'] = 'Maroon'
    metka['fg'] = 'SandyBrown'


window = Tk()


metka = Label(text='Keep moving on!',
             fg='Indigo',
             bg='Lavender',
             width=15,
             height=5,
             font='Arial 14 bold')
metka.pack()

knopka = Button(text='Изменить метку',
                width=15,
                height=3,
                font='Arial 14 bold')
knopka.config(command=change)
knopka.pack()


window.mainloop()