from tkinter import *

def swap():
    a = entry.get()
    b = entry2.get()

    entry.delete(0, END)
    entry2.delete(0, END)
    entry.insert(0, b)
    entry2.insert(0, a)

def swap_from_mem():
    if memory is not None:
        entry.delete(0, END)
        entry.insert(0, memory)

def add():
    try:
        a = int(entry.get())
        b = int(entry2.get())
        res.config(text=f'Результат: {a + b}', fg='black')
        global last_result
        last_result = a + b
    except ValueError:
        res.config(text='Ошибка: введите целые числа', fg='red')
        last_result = None

def subtract():
    try:
        a = int(entry.get())
        b = int(entry2.get())
        res.config(text=f'Результат: {a - b}', fg='black')
        global last_result
        last_result = a - b
    except ValueError:
        res.config(text='Ошибка: введите целые числа', fg='red')
        last_result = None

memory = None
last_result = None

def save():
    global memory
    if last_result is not None:
        memory = last_result
        mem_label.config(text=f'Память: {memory}')

root = Tk()
root.title('Мой калькулятор')
root.geometry("420x320")

msg = Label(root, text='Первое число')
msg.pack(pady=3)
entry = Entry(root, width=20)
entry.pack(pady=3)

msg2 = Label(root, text='Второе число')
msg2.pack(pady=3)
entry2 = Entry(root, width=20)
entry2.pack(pady=3)


frame = Frame(root)
frame.pack(pady=3)

b = Button(frame, text='Сложить', command=add)
b.pack(side=LEFT, padx=10, pady=3)
b2 = Button(frame, text='Вычесть', command=subtract)
b2.pack(side=LEFT, padx=10, pady=3)


res = Label(root, text='Результат: —')
res.pack(pady=3)


frame2 = Frame(root)
frame2.pack(pady=3)

b_swap = Button(frame2, text='Поменять местами', command=swap)
b_swap.pack()

#-------------------------------------------
mem_label = Label(text='Память: пуста')
mem_label.pack(pady=3)

#-------------------------------------------
frame_mem = Frame(root)
frame_mem.pack(pady=3)

b_mem1 = Button(frame_mem, text='В память', command=save)
b_mem1.pack(side=LEFT, padx=10, pady=3)
b_mem2 = Button(frame_mem, text='Из памяти', command=swap_from_mem)
b_mem2.pack(side=LEFT, padx=10, pady=3)

root.mainloop()