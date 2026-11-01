import shutil
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os

root = Tk()
root.withdraw()

direct = fd.askdirectory(title='Выберите папку для копирования')

if direct:
    new_dir = direct + '_new'
    if not os.path.exists(new_dir):
        try:
            shutil.copytree(direct, new_dir)
            mb.showinfo('Копирование', f'Все содержимое папки {direct} скопировано в папку {new_dir}')
            # print(f'Все содержимое папки {direct} скопировано в папку {new_dir}')
        except Exception as e:
            mb.showerror('Ошибка', f"Ошибка при копировании: {e}")
            # print(f"Ошибка при копировании: {e}")
    else:
        mb.showwarning('Невозможно скопировать', f"Папка {new_dir} уже существует")
        # print(f"Папка {new_dir} уже существует")
else:
    mb.showinfo('Копирование не произведено', 'Папка не была выбрана')
    # print('Папка не была выбрана')