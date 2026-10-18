from tkinter import *

def start():
    try:
        minutes = int(e.get())
    except ValueError:
        result.config(text="Это не число")
        return            # дальше не идём
    else:
        if 1 <= minutes <= 120:
            result.config(text=f'Таймер: {minutes} мин')
        else:
            result.config(text='Нужно от 1 до 120 минут')                   # проверка диапазона из задачи 07


root = Tk()
root.title('Таймер корма')
root.geometry('360x200')

Label(root, text='Сколько минут варить?').pack()

e = Entry(root)
e.pack()

b = Button(root, text='Запустить', command=start)
b.pack()

result = Label(root, text='Таймер не запущен')
result.pack()

root.mainloop()

