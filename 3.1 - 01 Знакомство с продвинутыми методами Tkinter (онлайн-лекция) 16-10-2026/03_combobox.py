from tkinter import *
from tkinter import ttk
from io import BytesIO

from PIL import Image, ImageTk
import requests

def load_image(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        img = Image.open(image_data)        # img - превращает в картинку
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)           # уменьшение картинки под окно
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Ошибка {e}')
        return None


def set_image():
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img


def open_new_window():
    # tag = tag_entry.get()
    tag = tag_combobox.get()
    url_with_tag = (f'https://cataas.com/cat/{tag}' if tag
                    else 'https://cataas.com/cat')
    img = load_image(url_with_tag)
    if img:
        new_window = Toplevel(root)
        new_window.title('Картинка с котиком')
        new_window.geometry('620x520')
        label = Label(new_window, image=img)
        label.image = img
        label.pack()


def exit_program():
    root.destroy()


ALLOWED_TAGS = ['sleep', 'jump', 'smile', 'fight', 'black', 'white',
                'ginger', 'siamese', 'bengal']


root = Tk()
root.title('Cats')
root.geometry('620x580')

label = Label()
label.pack()

menu_bar = Menu(root)
root.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit_program)

# tag_entry = Entry()
# tag_entry.pack()

tag_label = Label(text='Выбери тег')
tag_label.pack(side=BOTTOM, pady=5)

tag_combobox = ttk.Combobox(values=ALLOWED_TAGS)
tag_combobox.pack(side=BOTTOM, pady=5)

load_button = Button(text='Загрузить по тегу', command=open_new_window)
load_button.pack(side=BOTTOM, pady=5)

# update_btn = Button(text='Следующая картинка', command=set_image)
# update_btn.pack(pady=5, side=BOTTOM)

url = 'https://cataas.com/cat'
# img = load_image(url)
#
# if img:
#     label.config(image=img)
#     label.image = img


set_image()


root.mainloop()