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
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Ошибка {e}')
        return None

root = Tk()
root.title('Cats')
root.geometry('600x480')

label = Label()
label.pack()

url = 'https://cataas.com/cat'

img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

root.mainloop()