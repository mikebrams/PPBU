from tkinter import *


def calc():
    value = v.get()
    extra_value1 = vch1.get()
    extra_value2 = vch2.get()
    msg.config(text=f'Итого: {value + extra_value1 + extra_value2} жетонов')


root = Tk()
root.title('Заказ для мастерской')
root.geometry('560x460')


v = IntVar()
v.set(100)

vch1 = IntVar()
vch1.set(0)

vch2 = IntVar()
vch2.set(0)

frame = Frame(root)
frame.pack()

rb1 = Radiobutton(frame, text='Малый', variable=v, value=100, height=2)
rb1.grid(row=0, sticky='w')
rb2 = Radiobutton(frame, text='Большой', variable=v, value=160, height=2)
rb2.grid(row=1, sticky='w')

cb1 = Checkbutton(frame, text='Упаковка', height=2, variable=vch1, onvalue=20, offvalue=0)
cb1.grid(row=2, sticky='w')
cb2 = Checkbutton(frame, text='Срочно', height=2, variable=vch2, onvalue=40, offvalue=0)
cb2.grid(row=3, sticky='w')


calculate = Button(frame, text='Рассчитать', bg='RoyalBlue', fg='white', width=16, font='Arial 14 bold', height=1, command=calc)
calculate.grid(row=4, sticky='w', pady=3)

msg = Label(frame, text='Итого: —', bg='#ECFDF1', width=24, font='Arial 14 bold', height=1)
msg.grid(row=5, sticky='w', pady=3)


root.mainloop()