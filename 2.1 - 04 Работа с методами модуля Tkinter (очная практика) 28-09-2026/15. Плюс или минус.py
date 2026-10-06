from tkinter import *

def add():
    a = int(entry.get())
    b = int(entry2.get())
    msg3.config(text=f'Результат: {a + b}')

def subtract():
    a = int(entry.get())
    b = int(entry2.get())
    msg3.config(text=f'Результат: {a - b}')


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


msg3 = Label(root, text='Результат: —')
msg3.pack(pady=3)

root.mainloop()