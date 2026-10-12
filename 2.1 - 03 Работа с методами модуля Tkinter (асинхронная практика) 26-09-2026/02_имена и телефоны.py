from tkinter import *
from tkinter import messagebox as mb
def add_item():
    if s.get() == 0:
        lb1.insert(END, e.get())
    else:
        if validate_phone():
            lb2.insert(END, e.get())
            # mb.showinfo('Добавление номера', 'Номер телефона успешно добавлен')
    e.delete(0, END)

def del_item():
    if s.get() == 0:
        lb1.delete(ANCHOR)
    else:
        lb2.delete(ANCHOR)

def save():
    try:
        with open('phones.txt', 'w', encoding='utf-8') as f:
            for i in range(lb1.size()):
                f.write(f'{lb1.get(i)}: {lb2.get(i)}\n')
        mb.showinfo('Сохранение', 'Контакты успешно сохранены')
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка {e}')

def load():
    try:
        with open('phones.txt', 'r', encoding='utf=8') as f:
            lb1.delete(0, END)
            lb2.delete(0, END)
            for line in f:
                name, _, phone = line.partition(': ')
                lb1.insert(END, name)
                lb2.insert(END, phone)
        mb.showinfo('Загрузка', 'Контакты успешно загружены')
    except FileNotFoundError:
        mb.showerror('Ошибка', f'Файл не найден!')
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка {e}')

def validate_phone():
    number = e.get()
    if len(number) == 10 and number.isdigit() and number.startswith('9'):
        # mb.showinfo('Проверка', 'Номер телефона прошел проверку')
        return True
    else:
        mb.showerror('Ошибка', f'Номер телефона должен быть десятизначным, состоять из цифр и начинаться с "9"')
        return False

root = Tk()
root.title('Телефонная книга')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'400x200+{w//4}+{h//3}')


f1 = Frame()
f1.pack(side=LEFT)

title = Label(f1, text='Имена')
title.pack()
lb1 = Listbox(f1)
lb1.pack()

f2 = Frame()
f2.pack(side=LEFT)
title2 = Label(f2, text='Телефоны')
title2.pack()
lb2 = Listbox(f2)
lb2.pack()

f3 = Frame()
f3.pack(side=LEFT)


s = IntVar(value=0)

rb1 = Radiobutton(f3, text='Имена', value=0, variable=s)
rb1.pack()
rb2 = Radiobutton(f3, text='Телефоны', value=1, variable=s)
rb2.pack()

e = Entry(f3)
e.pack()

b1 = Button(f3, text='Добавить', command=add_item)
b1.pack()
b2 = Button(f3, text='Удалить', command=del_item)
b2.pack()
b3 = Button(f3, text='Сохранить контакт', command=save)
b3.pack()

b4 = Button(f3, text='Загрузить контакты', command=load)
b4.pack()


root.mainloop()