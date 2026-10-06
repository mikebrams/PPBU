from tkinter import *
from tkinter import messagebox as mb

def summ():
    s1 = e1.get()
    if not s1.strip('-').isdigit():
        mb.showerror(title='Ошибка', message='В первое поле должно быть введено целое число')
        return
    s2 = e2.get()
    if not s2.strip('-').isdigit():
        mb.showerror(title='Ошибка', message='Во второе поле должно быть введено целое число')
        return

    s_1 = int(s1)
    s_2 = int(s2)

    res = s_1 + s_2

    m1.config(text=f'{s_1} + {s_2} = {str(res)}')

    answer = mb.askretrycancel('Вопрос', 'Сложить еще два числа?')
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        m1['text'] = ''
    else:
        root.destroy()


root = Tk()
root.title('Калькулятор')

m = Label(text='Введите 2 целых числа и нажмите на кнопку', height=3)
m.pack()


e1 = Entry()
e1.pack()
e2 = Entry()
e2.pack()

b1 = Button(text='Сложить два числа', command=summ)
b1.pack()

m1 = Label(text='', height=3)
m1.pack()

root.mainloop()
