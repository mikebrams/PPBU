import os
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
import requests


def get_dog_image(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()  # проверка - получили ли JSON
        data = resp.json()  # получили словарь
        print(data['message'])
        return data['message']
    except Exception as err:
        print(f'Ошибка чтения API: {err}')
        return None


def show_image():
    global image_s
    image_url = get_dog_image('https://dog.ceo/api/breeds/image/random')
    try:
        resp = requests.get(image_url)  # получаем ответ от запроса
        resp.raise_for_status()  # проверка корректности ответа - код 200, если нет, то уходим в Ex
        image_data = BytesIO(resp.content)  # из бинарного контента вытягиваем данные только картинки в бинарном виде
        image_s = Image.open(image_data)  # преобразуем в картинку из бинарных данных

        image = image_s
        image.thumbnail((600, 480), Image.Resampling.LANCZOS)  # делаем ресайз до размера
        image = ImageTk.PhotoImage(image)  # преобразуем картинку для возможности просмотра в Tkinter
        label.config(image=image)  # вешаем на лейбл
        label.image = image  # фиксация картинки на глобальной области видимости

    except Exception as err:
        print(f'Ошибка загрузки: {err}')
        return None


def save_image():
    global image_s
    if image_s is None:
        mb.showinfo('Картинка', 'Отсутствие загруженного изображения')
        return

    def_name = os.path.basename(name_file)  # получения только имени файла без папок, слэшей и т.д.
    fp = filedialog.asksaveasfilename(
        defaultextension='.png',
        filetypes=[('PNG', '*.png'),
                   ('JPEG', '*.jpg'),
                   ('All files', '*.*')],
        initialfile=def_name
    )

    if fp:
        image_s.save(fp)
        mb.showinfo('Сохранение файла', f'Сохранено в папке: {fp}')

image_s = ''
name_file = 'image_'
root = Tk()
root.title('Dogs')
root.geometry('620x550')

label = Label(root)
label.pack()

btn = Button(root, text='Загрузить', command=show_image)
btn.pack(pady=5)

save_btn = Button(root, text='Сохранить', command=save_image)
save_btn.pack(pady=5)

show_image()
root.mainloop()
