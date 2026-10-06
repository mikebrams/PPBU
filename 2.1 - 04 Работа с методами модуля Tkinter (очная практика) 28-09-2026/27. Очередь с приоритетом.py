from tkinter import *

case = 0

def add():
    mode = ['Обычно:', 'Срочно:']
    title_get = title.get().strip()

    if title_get:
        entry_get = title.get().strip()

        box.insert(END, f'{mode[vch1.get()]} {entry_get}')
        title.delete(0, END)

        global case
        case += 1
        msg.config(text=f'Дел: {case}')

def remove_selected():
    selected = box.curselection()
    if selected:
        i = selected[0]
        box.delete(i)

        global case
        case -= 1
        msg.config(text=f'Дел: {case}')

def move_up():
    selected = box.curselection()
    if selected:
        i = selected[0]
        if i > 0:
            text = box.get(i)
            box.delete(i)
            box.insert(i - 1, text)
            box.selection_set(i - 1)

root = Tk()
root.title('Очередь с приоритетом')
root.geometry('620x520')

title = Entry(root)
title.pack(fill='x', padx=10, pady=10)


frame = Frame(root)
frame.pack(fill='none', padx=10, pady=10)

vch1 = BooleanVar()
vch1.set(False)
urgent = Checkbutton(frame, text='Срочно', height=2, variable=vch1, onvalue=True, offvalue=False)
urgent.grid(row=0, sticky='we', pady=3, padx=10, column=0)
add_title = Button(frame, text='Добавить', bg='RoyalBlue', fg='white', font='Arial 10 bold', height=1, command=add)
add_title.grid(row=0, sticky='we', pady=3, padx=10, column=1)


box = Listbox()
box.pack(fill='x', padx=10, pady=10)

frame3 = Frame(root)
frame3.pack(fill='none', padx=10, pady=10)

remove = Button(frame3, text='Удалить', bg='RoyalBlue', fg='white', font='Arial 10 bold', height=1, command=remove_selected)
remove.grid(row=0, sticky='we', padx=10, column=0)
up = Button(frame3, text='Вверх', bg='RoyalBlue', fg='white', font='Arial 10 bold', height=1, command=move_up)
up.grid(row=0, sticky='we', padx=10, column=1)


msg = Label(root, text='Дел: 0', bg='#ECFDF1', font='Arial 10 bold', height=1)
msg.pack(fill='x', padx=10, pady=10)


root.mainloop()