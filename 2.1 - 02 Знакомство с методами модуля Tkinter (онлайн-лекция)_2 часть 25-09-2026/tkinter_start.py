from tkinter import *


def answer(event):
    answ = num.get().strip()  # считывает значение из виджета
    result.configure(text=answ)


root = Tk()  # создаем объект нового окна
root.title('Старт')  # название главного окна (в левом верхнем углу)
# WIDTH = root.winfo_screenmmwidth()
WIDTH = root.winfo_screenmmwidth()
HEIGHT = root.winfo_screenheight()
print(WIDTH, HEIGHT)
X = 300
Y = 140

root.geometry(
    f'{X}x{Y}+{WIDTH // 2 - X // 2}+{HEIGHT // 2 - Y // 2 - 25}')  # изменение размера главного окна + позиция вывода окна на мониторе
# root.geometry('300x100+1000+200')        # изменение размера главного окна + позиция вывода окна на мониторе

prompt = Label(text='Введите значение', font='Arial 15')  # создание запроса
prompt.pack(side=TOP)  # размещение запроса в главном окне

# prompt2 = Label(text='Введите значение 2')              # создание запроса
# prompt2.pack(side=RIGHT)                                # размещение запроса в главном окне

# pack() = pack(side=TOP)      - размещает сверху по умолчанию
# pack(side=LEFT [, BOTTOM, RIGHT, LEFT)     размещает сверху        = pack(side=TOP)

num = Entry(width=5, font='Arial 15', justify='center')  # ВИДЖЕТ - создание окошка для ввода
num.pack()

result = Label(text='    ', font='Arial 15', bg='lightgray')
result.pack(pady=10)

btn = Button(text='Выполнить', command=answer)
btn.pack()

num.bind('<Return>', answer)

root.mainloop()


