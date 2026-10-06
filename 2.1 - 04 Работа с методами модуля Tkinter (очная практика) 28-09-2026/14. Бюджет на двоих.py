from tkinter import *

def calc():
    a = int(entry.get())
    b = int(entry2.get())

    res = a + b
    msg3.config(text=f'Результат: {res}')

root = Tk()
root.title('Мой калькулятор')
root.geometry("420x320")

msg = Label(root, text='Первое число')
msg.pack(pady=5)

entry = Entry(root, width=20)
entry.pack(pady=5)

msg2 = Label(root, text='Второе число')
msg2.pack(pady=5)

entry2 = Entry(root, width=20)
entry2.pack(pady=5)

b = Button(text='Сложить', command=calc)
b.pack(pady=5)

msg3 = Label(root, text='Результат: —')
msg3.pack(pady=5)

root.mainloop()