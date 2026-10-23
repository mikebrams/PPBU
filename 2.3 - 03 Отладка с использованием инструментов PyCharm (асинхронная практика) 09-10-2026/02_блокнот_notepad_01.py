from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def delete():
    text.delete(1.0, END)

def insert():
    try:
        file = fd.askopenfilename()
        if file:  # Проверяем, выбран ли файл
            with open(file, 'r', encoding='utf-8') as f:
                s = f.read()
            text.insert(1.0, s)
    except FileNotFoundError:
        mb.showerror("Ошибка", "Файл не найден")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")

def save():
    try:
        file = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", "*.html;*.htm"),
                       ("All files", "*.*")))
        if file:  # Проверяем, выбран ли файл
            with open(file, 'w') as f:
                s = text.get(1.0, END)
                f.write(s)
    except FileNotFoundError:
        mb.showerror("Ошибка", "Не удалось сохранить файл")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")

def quit():
    root.destroy()

root = Tk()
text = Text(root, width=30, height=8, bg="gray", wrap=WORD)
text.pack(side=LEFT)
scroll = Scrollbar(root, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Открыть', command=insert)
file_menu.add_command(label='Сохранить', command=save)
file_menu.add_command(label='Удалить', command=delete)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=quit)


root.mainloop()
