from tkinter import *

pen_color = 'black'

def draw(event):
    """Функция рисования на холсте"""
    # при нажатии левой клавиши мыши и движении в x, y передаются координаты курсора
    x, y = event.x, event.y
    # создается овал в квадрате с координатами x, y - верхняя левая точка, x + 5, y + 5 - нижняя правая точка
    canvas.create_oval(x, y, x + 5, y + 5, fill=pen_color, outline=pen_color)

def change_to_red(event):
    """Функция для изменения цвета на красный
    C помощью метода bind между собой связываются виджет, событие и действие.
    Например, виджет – кнопка, событие – клик по ней левой кнопкой мыши,
    действие – отправка сообщения"""
    global pen_color
    pen_color = 'red'

root = Tk()
root.title('Графический редактор')

canvas = Canvas(root, width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

red_label = Label(root, text='', bg='red', width=8, height=2)
red_label.pack(side=LEFT)
red_label.bind("<Button-1>", change_to_red)


root.mainloop()
