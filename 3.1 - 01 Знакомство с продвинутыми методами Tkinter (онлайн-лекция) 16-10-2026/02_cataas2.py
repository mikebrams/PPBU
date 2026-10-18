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

root = Tk()
root.title('Cats')
root.geometry('620x520')

label = Label()
label.pack()

update_btn = Button(text='Следующая картинка', command=set_image)
update_btn.pack(pady=5, side=BOTTOM)

url = 'https://cataas.com/cat'
# img = load_image(url)
#
# if img:
#     label.config(image=img)
#     label.image = img


set_image()


root.mainloop()