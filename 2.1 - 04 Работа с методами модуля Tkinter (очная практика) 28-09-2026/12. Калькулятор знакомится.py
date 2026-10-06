from tkinter import *

def show_name():
    name = entry.get().strip()
    if name:
        msg.config(text=f'Привет, {name}!')
    else:
        msg.config(text='Привет, гость!')

root = Tk()
root.title('Мой калькулятор')
root.geometry("420x320")

entry = Entry(root, width=20)
entry.pack(pady=5)

b = Button(text='Поздороваться', command=show_name)
b.pack(pady=5)

msg = Label(root, text='Привет!')
msg.pack(pady=5)

root.mainloop()