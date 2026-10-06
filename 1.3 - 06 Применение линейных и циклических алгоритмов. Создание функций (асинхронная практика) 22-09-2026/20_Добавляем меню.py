from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd


def delete():
    text.delete(1.0, END)


def insert():
    try:
        file = fd.askopenfilename()
        if file:
            with open(file, 'r') as f:
                s = f.read()
                text.insert(1.0, s)
    except FileNotFoundError:
        mb.showerror('Ошибка', 'Файл не найден')
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка {e}')


def save():
    try:
        file = fd.asksaveasfilename(
            filetypes=(('TXT files', '*.txt'),
                       ('All files', '*.*')
                       ))
        if file:
            with open(file, 'w') as f:
                s = text.get(1.0, END)
                f.write(s)
    except FileNotFoundError:
        mb.showerror('Ошибка', 'Файл не найден')
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка {e}')

def quit():
    window.destroy()


window = Tk()
window.title('Title')

# создание меню
mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Открыть', command=insert)
filemenu.add_command(label='Новый', command=delete)
filemenu.add_command(label='Сохранить', command=save)
filemenu.add_separator()
filemenu.add_command(label='Выход', command=quit)
mainmenu.add_cascade(label='Файл', menu=filemenu)




# создание многострочного текстового поля
text = Text(width=60, height=20, bg='gray', fg='white', font='Arial 12 bold', wrap=WORD)
text.pack(side=LEFT)

scroll = Scrollbar(command=text.yview)        # создание полосы прокрутки
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

# b = Button(text='Открыть файл', command=insert)
# b.pack()
#
# b2 = Button(text='Удаление текста', command=delete)
# b2.pack(side=LEFT)
#
# b3 = Button(text='Сохранить', command=save)
# b3.pack(side=LEFT)



window.mainloop()