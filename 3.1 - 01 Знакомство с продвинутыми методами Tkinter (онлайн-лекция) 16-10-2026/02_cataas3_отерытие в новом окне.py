from tkinter import *
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


def exit_program():
    root.destroy()


def open_new_window():
    tag = tag_entry.get()
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


root = Tk()
root.title('Cats')
root.geometry('620x540')

label = Label()
label.pack()

menu_bar = Menu(root)
root.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit_program)

tag_entry = Entry()
tag_entry.pack()

load_button = Button(text='Загрузить по тегу', command=open_new_window)
load_button.pack()

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