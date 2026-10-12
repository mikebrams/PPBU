from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import Image, ImageTk, ImageGrab


def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x-ps_default, y-ps_default, x + ps_default, y + ps_default, fill=pen_color, outline=pen_color)


def load_image():
    try:
        file_path = fd.askopenfilename(title='Выбрать файл',
                                       filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
        if file_path:
            image = Image.open(file_path)           # Открываем картинку
            image = image.resize((600, 400))        # Подгоняем ее под размер окна
            image_tk = ImageTk.PhotoImage(image)    # Преобразование картинки под интерфейс Tk
            canvas.create_image(0, 0, anchor=NW, image=image_tk)
            canvas.image = image_tk
    except Exception as e:
        mb.showerror('Ошибка', f'Не удалось загрузить файл из-за ошибки:\n{e}')


def save_image():
    try:
        file_path = fd.asksaveasfilename(defaultextension='*.png', filetypes=[('PNG files', '*.png')])
        if file_path:
            x = root.winfo_rootx() + canvas.winfo_x()
            y = root.winfo_rooty() + canvas.winfo_y()
            x1 = x + canvas.winfo_width()
            y1 = y + canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
            mb.showinfo('Сохранено', 'Изображение успешно сохранено.')
    except Exception as e:
        mb.showerror('Ошибка', f'Не удалось сохранить файл из-за ошибки:\n{e}')

def set_pen_size():
    global ps_default
    try:
        s = entry_pen_size.get()
        s_entry = int(s)
        if 1 <= s_entry <= 50:
            ps_default = s_entry // 2
        else:
            mb.showinfo('Толщина линии', 'Толщина линии должна быть от 1 до 50')
    except ValueError:
        mb.showerror('Ошибка', f'Чтобы установить толщину введите целое число от 1 до 50')


def clear_canvas():
    canvas.delete("all")


def quit_editor():
    root.destroy()


root = Tk()
root.title('Графический редактор')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w2 = w // 4 - 300
h2 = h // 3 - 200
root.geometry(f'610x440+{w2}+{h2}')

mainmenu = Menu(root)           # основное меню
root.config(menu=mainmenu)
file_menu = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label='Файл', menu=file_menu)   # подвязывание к главному меню
file_menu.add_command(label='Загрузить изображение', command=load_image)
file_menu.add_command(label='Сохранить изображение', command=save_image)
file_menu.add_command(label='Очистить изображение', command=clear_canvas)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=quit_editor)

canvas = Canvas(root, width=600, height=400, bg='WhiteSmoke')
canvas.pack()
canvas.bind("<B1-Motion>", draw)

pen_color = 'black'
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'DarkViolet', 'gray', 'black']
for color in colors:
    lbl = Label(root, bg=color, width=5, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<Button-1>", lambda e, c=color: globals().update(pen_color=c))

ps_default = 5 // 2
pen_size = Label(text='Толщина линии:')
pen_size.pack(side=LEFT, padx=2)

entry_pen_size = Entry(width=6)
entry_pen_size.insert(0, '5')
entry_pen_size.pack(side=LEFT, padx=2)

set_ps = Button(text='Установить толщину', command=set_pen_size)
set_ps.pack(side=LEFT, padx=2)

root.mainloop()
