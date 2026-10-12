from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk


def draw(event):
    """Функция рисования на холсте"""
    # при нажатии левой клавиши мыши и движении в x, y передаются координаты курсора
    x, y = event.x, event.y
    # создается овал в квадрате с координатами x, y - верхняя левая точка, x + 5, y + 5 - нижняя правая точка
    canvas.create_oval(x, y, x + 5, y + 5, fill=pen_color, outline=pen_color)

root = Tk()
root.title('Графический редактор')

pen_color = 'red'
canvas = Canvas(root, width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)


colors = ['red', 'green', 'blue', 'black']
for color in colors:
    lbl = Label(root, text='', bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<Button-1>", lambda e, c=color: globals().update(pen_color=c))


root.mainloop()
