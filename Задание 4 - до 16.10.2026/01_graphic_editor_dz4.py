from tkinter import *


def draw(event):
    """Функция рисования на холсте"""
    # при нажатии левой клавиши мыши и движении в x, y передаются координаты курсора
    x, y = event.x, event.y
    # создается овал в квадрате с координатами x, y - верхняя левая точка, x + 5, y + 5 - нижняя правая точка
    canvas.create_oval(x, y, x + 5, y + 5, fill='red', outline='red')


root = Tk()
root.title('Графический редактор')

canvas = Canvas(root, width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

root.mainloop()