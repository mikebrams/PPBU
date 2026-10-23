from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from transliterate import translit
from googletrans import Translator, LANGUAGES

def delete():
    text.delete(1.0, END)
    update_status()


def transliter():
    try:
        source_text = text.get(1.0, END)
        t_text = translit(source_text, 'ru', reversed=True)
        text.delete(1.0, END)
        text.insert(1.0, t_text)
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка {e}')
    update_status()

def translate():
    try:
        source_text = text.get(1.0, END)
        translator = Translator()
        translated_text = translator.translate(source_text, src='ru', dest='en').text
        text.delete(1.0, END)
        text.insert(1.0, translated_text)
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка при переводе: {e}")


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
    update_status()

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


def update_status():
    content = text.get(1.0, 'end-1c')
    char_count = len(content)
    word_count = len(content.split())
    status_label.config(text=f'Символов: {char_count} Слов: {word_count}')


def quit():
    root.destroy()


root = Tk()

frame = Frame()
frame.pack()

text = Text(frame, width=30, height=8, bg="gray", wrap=WORD)
text.pack(side=LEFT)
text.bind('<Key>', lambda event: update_status())

scroll = Scrollbar(frame, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

status_label = Label(text='proba', anchor=W)
status_label.pack(fill=X)

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Открыть', command=insert)
file_menu.add_command(label='Сохранить', command=save)
file_menu.add_command(label='Удалить', command=delete)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=quit)

process_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Обработка', menu=process_menu)
process_menu.add_command(label='Транслитерация', command=transliter)
process_menu.add_command(label='Перевод на английский', command=translate)


update_status()

root.mainloop()
