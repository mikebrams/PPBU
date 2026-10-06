from tkinter import *

def read():
    name = e.get() # получение текста из поля ввода
    print(name)
    e.delete(0, END)        # очистка поля ввода после печати в консоль с первого символа до конца строки

def read2():
    city = e2.get() # получение текста из поля ввода
    print(city)
    e2.delete(0, END)        # очистка поля ввода после печати в консоль с первого символа до конца строки

window = Tk()

frame = Frame(window)           # если не указать window, то будет размещен в нем по умолчанию
frame.pack()

frame2 = Frame(window)
frame2.pack()

m = Label(frame, text='Введите имя:', bg='gray', fg='white', font='Courier 24 bold')
m.pack(side=LEFT)

e = Entry(frame, width=25, justify='left', bg='gray', fg='white', font='Courier 24 bold')   # поле ввода, ширина, выравнивание текста ввода
e.pack(side=LEFT)

b = Button(frame, text='Ввод:', width=12, bg='gray', fg='white', font='Courier 24 bold',
           command=read)
b.pack(side=LEFT)



m2 = Label(frame2, text='Введите город:', bg='gray', fg='white', font='Courier 24 bold')
m2.pack(side=LEFT)

e2 = Entry(frame2, width=25, justify='left', bg='gray', fg='white', font='Courier 24 bold')   # поле ввода, ширина, выравнивание текста ввода
e2.pack(side=LEFT)

b2 = Button(frame2, text='Ввод:', width=12, bg='gray', fg='white', font='Courier 24 bold',
           command=read2)
b2.pack(side=LEFT)




window.mainloop()
