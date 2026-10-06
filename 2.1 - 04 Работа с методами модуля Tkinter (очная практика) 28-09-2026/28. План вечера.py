from tkinter import *

case = 0
minutes = 0

def add():
    mode = ['обычно', 'срочно']
    title_get = title.get().strip()

    if title_get:
        box.insert(END, f'{v.get()} мин | {mode[vch1.get()]} | {title_get}')
        title.delete(0, END)

        global case
        global minutes
        minutes_get = v.get()
        case += 1
        minutes += minutes_get
        msg.config(text=f'Дел: {case} | Время: {minutes} мин')


def remove_():
    selected = box.curselection()
    if selected:
        i = selected[0]
        global case
        global minutes
        minutes_get = int(box.get(i).split()[0])
        case -= 1
        minutes -= minutes_get
        msg.config(text=f'Дел: {case} | Время: {minutes} мин')
        box.delete(i)

def up_():
    selected = box.curselection()
    if selected:
        i = selected[0]
        if i > 0:
            text = box.get(i)
            box.delete(i)
            box.insert(i - 1, text)
            box.selection_set(i - 1)

def clean_():
    box.delete(0, END)
    msg.config(text=f'Дел: 0 | Время: 0 мин')
    global minutes
    global case
    minutes = 0
    case = 0


root = Tk()
root.title('План вечера')
root.geometry('680x620')

title = Entry(root)
title.pack(fill='x', padx=10, pady=10)

frame = Frame(root)
frame.pack(fill='x', padx=10, pady=10)

vch1 = BooleanVar()
vch1.set(False)
urgent = Checkbutton(frame, text='Срочно', height=2, variable=vch1, onvalue=True, offvalue=False)
urgent.grid(sticky='w', pady=3, padx=10, row=0, column=0)

v = IntVar()
v.set(30)

rb1 = Radiobutton(frame, text='15 мин', variable=v, value=15, height=2)
rb1.grid(row=1, column=0, sticky='w')
rb2 = Radiobutton(frame, text='30 мин', variable=v, value=30, height=2)
rb2.grid(row=1, column=1, sticky='w')
rb2 = Radiobutton(frame, text='45 мин', variable=v, value=45, height=2)
rb2.grid(row=1, column=2, sticky='w')

add_title = Button(frame, text='Добавить', bg='RoyalBlue', fg='white', font='Arial 10 bold', height=1, command=add)
add_title.grid(row=2, column=1, sticky='we', pady=3, padx=10)

box = Listbox()
box.pack(fill='x', padx=10, pady=10)

frame3 = Frame(root)
frame3.pack(fill='none', padx=10, pady=10)

remove = Button(frame3, text='Удалить', bg='RoyalBlue', fg='white', font='Arial 10 bold', height=1, command=remove_)
remove.grid(row=0, sticky='we', padx=10, column=0)
up = Button(frame3, text='Вверх', bg='RoyalBlue', fg='white', font='Arial 10 bold', height=1, command=up_)
up.grid(row=0, sticky='we', padx=10, column=1)
clean = Button(frame3, text='Очистить план', bg='RoyalBlue', fg='white', font='Arial 10 bold', height=1, command=clean_)
clean.grid(row=0, sticky='we', padx=10, column=2)

msg = Label(root, text='Дел: 0 | Время: 0 мин', bg='#ECFDF1', font='Arial 10 bold', height=1)
msg.pack(fill='x', padx=10, pady=10)

root.mainloop()