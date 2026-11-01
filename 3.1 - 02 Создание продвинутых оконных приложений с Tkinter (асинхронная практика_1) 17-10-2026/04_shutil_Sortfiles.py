import shutil
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os
from datetime import datetime



def choose_dir():
    direct = fd.askdirectory(title='Выберите папку с изображениями для их копирования')
    if direct:
        organize_photos(direct)

def organize_photos(directory):
    for file in os.listdir(directory):
        if file.lower().endswith(('.jpg' '.jpeg', '.png', '.bmp', '.tiff')):
            filepath = os.path.join(directory, file)
            timestamp = os.path.getmtime(filepath)
            date = datetime.fromtimestamp(timestamp)
            year_month = date.strftime("%Y_%m")
            new_dir = os.path.join(directory, year_month)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            shutil.move(filepath, os.path.join(new_dir, file))
    mb.showinfo('Успех!', 'Все фотографии рассортированы')


root = Tk()
root.withdraw()

choose_dir()

root.mainloop()