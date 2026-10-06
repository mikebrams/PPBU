from tkinter import *
from tkinter import messagebox as mb


def calc(action=None):
    ent1 = e1.get()
    if not ent1.strip('-').isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено целое число")
        return
    ent2 = e2.get()
    if not ent2.strip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено целое число")
        return
    ent3 = e3.get()
    if not ent3.strip('-').isdigit():
        mb.showerror("Ошибка", "В третье поле должно быть введено целое число")
        return

    num1 = int(ent1)
    num2 = int(ent2)
    num3 = int(ent3)

    if action == 'Сложить':
        res = num1 + num2 + num3
        msg.config(text=f'{num1} + {num2} + {num3} = {str(res)}')
    if action == 'Умножить':
        res = num1 * num2 * num3
        msg.config(text=f'{num1} * {num2} * {num3} = {str(res)}')

    answer = mb.askretrycancel(title="Вопрос", message="Сложить или умножить еще три числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        msg.config(text='')
    else:
        window.destroy()

#--------------------------------------------------------------------------------------------

window = Tk()
window.title('Калькулятор')

w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w2 = w//4 - 200
h2 = h//3 - 150
window.geometry(f"400x300+{w2}+{h2}")

box = Frame(window)
box.pack()

Label(box, text='Введите три числа и нажмите на кнопку:', font='Helvetica 9 bold').grid(row=0)
Label(box, text=chr(8212) * 27, fg='#ADADAD').grid(row=1)      # горизонтальная линия
Label(box, text='"Сложить три числа"\t- для вычисления суммы').grid(row=2, sticky='w')
Label(box, text='"Умножить три числа"\t- для вычисления произведения').grid(row=3, sticky='w')

e1 = Entry(width=25)
e1.pack(pady=3)
e2 = Entry(width=25)
e2.pack(pady=3)
e3 = Entry(width=25)
e3.pack(pady=3)

b1 = Button(text='Сложить три числа', command=lambda: calc('Сложить'), width=21)
b1.pack(pady=3)
b2 = Button(text='Умножить три числа', command=lambda: calc('Умножить'), width=21)
b2.pack(pady=3)

msg = Label(bg='#E6E6E6', width=45, font='Helvetica 9 bold')
msg.pack(pady=15)

window.mainloop()
