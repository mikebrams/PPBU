from tkinter import *

a = 0

def decrement():
    global a
    a -= 1
    metka['text'] = f'--- {a} ---'

def increment():
    global a
    a += 1
    metka['text'] = f'--- {a} ---'

window = Tk()
window.title('Уменьшение/увеличение числа')
metka = Label(text='-----0-----',
              width=40,
              height=5,
              bg='SlateGray',
              fg='Azure',
              font='Times 16 bold italic')
metka.pack()

knopka2 = Button(text='Увеличение',
                 width=40,
                 height=5,
                 bg='Gainsboro',
                 fg='green',
                 font='Times 16 bold italic')
knopka2.config(command=increment)
knopka2.pack()

knopka = Button(text='Уменьшение',
                width=40,
                height=5,
                bg='Gainsboro',
                fg='red',
                font='Times 16 bold italic')
knopka.config(command=decrement)
knopka.pack()



window.mainloop()