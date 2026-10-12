from tkinter import *

root = Tk()


def change_font(event, font):
    l['font'] = font

l = Label(text='Hello World')

l.bind('<Button-1>', lambda e: change_font(e, 'Verdana'))
l.bind('<Button-3>', lambda e: change_font(e, 'Times'))
l.pack()

root.mainloop()
