import tkinter as tk
from tkinter import messagebox

def new_file():
    messagebox.showinfo("Новый файл", "Создание нового файла.")

def open_file():
    messagebox.showinfo("Открыть файл", "Открытие файла.")

def about():
    messagebox.showinfo("О программе", "Пример меню в Tkinter.")

root = tk.Tk()
root.title("Пример меню")
root.geometry("300x200")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)
menu_bar.add_cascade(label="Файл", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="О программе", command=about)

menu_bar.add_cascade(label="Справка", menu=help_menu)

root.mainloop()

