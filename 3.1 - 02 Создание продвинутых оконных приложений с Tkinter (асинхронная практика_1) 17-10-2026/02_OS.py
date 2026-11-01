from tkinter import *
from tkinter import filedialog as fd
from datetime import datetime
import os

root = Tk()
root.withdraw()

direct = fd.askdirectory()

if direct:
    for file in os.listdir(direct):  # вывод в консоль список файлов в выбранной директории
        if file.lower().endswith(('.jpg' '.jpeg', '.png', '.bmp', '.tiff', '.txt')):
            filepath = os.path.join(direct, file)   # склеивание директории и файла
            lt = os.path.getmtime(filepath)         # время создания файла в секундах от 01.01.1970
            ft = datetime.fromtimestamp(lt).strftime("%d-%m-%Y")    # время создания файла переведенное в текущее время
            print(f'{file}, {ft}')

root.mainloop()