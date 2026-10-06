from tkinter import *


def reserve():
    time_res = level.get()
    msg.config(text=f'План: {time_res} мин')


root = Tk()
root.title('Запас времени')
root.geometry('520x420')

level = Scale(root, from_=5, to=60, resolution=5, orient="horizontal", length=300)
level.set(25)
level.pack()

plan = Button(root, text='Запланировать', bg='RoyalBlue', fg='white', width=24, font='Arial 14 bold', command=reserve)
plan.pack(pady=5)


msg = Label(root, text='План: не задан', bg='#ECFDF1', width=24, font='Arial 14 bold')
msg.pack(pady=15)

root.mainloop()