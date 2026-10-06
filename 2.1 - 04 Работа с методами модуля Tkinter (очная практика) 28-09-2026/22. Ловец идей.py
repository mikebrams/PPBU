from tkinter import *

idea = 0

def move_to():
    entry_get = entry_window.get().strip()

    if entry_get:

        box.insert(END, entry_get)
        entry_window.delete(0, END)

        global idea
        idea += 1
        msg.config(text=f'Идей: {idea}')

root = Tk()
root.title('Ловец идей')
root.geometry('520x480')

entry_window = Entry(width=49)
entry_window.pack(pady=3)

add = Button(root, text='Добавить', bg='RoyalBlue', fg='white', width=24, font='Arial 14 bold', command=move_to)
add.pack(pady=5)


box = Listbox(width=49)
box.pack()

msg = Label(root, text='Идей: 0', bg='#ECFDF1', width=24, font='Arial 14 bold')
msg.pack(pady=15)

root.mainloop()