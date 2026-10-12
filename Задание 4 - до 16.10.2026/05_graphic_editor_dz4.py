from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import Image, ImageTk, ImageGrab


def draw(event):
    """Функция рисования на холсте"""
    # при нажатии левой клавиши мыши и движении в x, y передаются координаты курсора
    x, y = event.x, event.y
    # создается овал в квадрате с координатами x, y - верхняя левая точка, x + 5, y + 5 - нижняя правая точка
    canvas.create_oval(x, y, x + 5, y + 5, fill=pen_color, outline=pen_color)


def load_image():
    try:
        file_path = fd.askopenfilename(title='Выбрать файл',
                                       filetypes=[('Image files','*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((600, 400))
            image_tk = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, anchor=NW, image=image_tk)
            canvas.image = image_tk
    except Exception as e:
        mb.showerror('Ошибка', f'Не удалось загрузить:\n{e}')

def save_canvas():
    try:
        file_path = fd.asksaveasfilename(defaultextension='.png', filetypes=[('PNG files', '*.png')])
        if file_path:
            x = root.winfo_rootx() + canvas.winfo_x()
            y = root.winfo_rooty() + canvas.winfo_y()
            x1 = x + canvas.winfo_width()
            y1 = y + canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
            mb.showinfo('Сохранено!', 'Изображение успешно сохранено.')
    except Exception as e:
        mb.showerror('Ошибка', f'Не удалось загрузить:\n{e}')

# image = 'Pencil.ico'
root = Tk()
root.title('Графический редактор')
# root.iconbitmap(image)

pen_color = 'red'
canvas = Canvas(root, width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)


colors = ['red', 'green', 'blue', 'black']
for color in colors:
    lbl = Label(root, text='', bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<Button-1>", lambda e, c=color: globals().update(pen_color=c))

Button(root, text='Загрузить изображение', command=load_image).pack()
Button(root, text='Сохранить холст', command=save_canvas).pack()

root.mainloop()
