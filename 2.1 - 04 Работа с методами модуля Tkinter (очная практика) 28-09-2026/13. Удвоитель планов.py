from tkinter import *

def calc():
    x = int(entry.get())
    y = x * 2
    msg.config(text=f'Результат: {y}')

root = Tk()
root.title('Мой калькулятор')
root.geometry("420x320")

entry = Entry(root, width=20)
entry.pack(pady=5)

b = Button(text='Удвоить', command=calc)
b.pack(pady=5)

msg = Label(root, text='Результат: —')
msg.pack(pady=5)

root.mainloop()