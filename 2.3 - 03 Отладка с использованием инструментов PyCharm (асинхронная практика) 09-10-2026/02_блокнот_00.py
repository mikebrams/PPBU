from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def delete():
    text.delete(1.0, END)

def insert():
    try:
        file = fd.askopenfilename()
        if file:  # Проверяем, выбран ли файл
            with open(file, 'r') as f:
                s = f.read()
            text.insert(1.0, s)
    except FileNotFoundError:
        mb.showerror("Ошибка", "Файл не найден")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")

from tkinter import messagebox

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

window = Tk()
text = Text(window, width=30, height=8, bg="gray", wrap=WORD)
text.pack(side=LEFT)
scroll = Scrollbar(window, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
b1 = Button(window, text="Открыть файл", command=insert)
b1.pack(side=LEFT)
b2 = Button(window, text="Удаление текста", command=delete)
b2.pack(side=LEFT)
b3 = Button(text="Сохранить файл", command=save)
b3.pack(side=LEFT)
window.mainloop()
