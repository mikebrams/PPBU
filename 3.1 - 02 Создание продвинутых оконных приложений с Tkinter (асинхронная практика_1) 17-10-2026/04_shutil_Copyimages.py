import shutil
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os

root = Tk()
root.withdraw()

direct = fd.askdirectory(title='Выберите папку с изображениями для их копирования')

if direct:
    new_dir = direct + '_new'
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    else:
        mb.showwarning('Невозможно создать папку', f"Папка {new_dir} уже существует")
    for file in os.listdir(direct):
        if file.lower().endswith(('.jpg' '.jpeg', '.png', '.bmp', '.tiff')):
            source_file = os.path.join(direct, file)
            destination_file = os.path.join(new_dir, file)
            try:
                shutil.move(source_file, destination_file)
                mb.showinfo('Копирование произведено', f'Файл {file} скопирован')
            except Exception as e:
                mb.showerror('Ошибка', f"Ошибка при копировании файла {file}: {e}")
    mb.showinfo('Успех', 'Все скопировано')
else:
    mb.showinfo('Копирование не произведено', 'Папка не была выбрана')
