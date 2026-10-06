from tkinter import *
from tkinter import messagebox as mb
import time

import pygame as pg

pg.mixer.init()
pg.mixer.music.load('music.mp3')


def tick():
    global time_alarm
    current_time = time.strftime('%H:%M:%S')
    if time_alarm == current_time or\
        time_alarm == time.strftime('%H:%M') or\
        time_alarm == time.strftime('%H'):
        time_alarm = ''
        pg.mixer.music.play()


    screen_time.after(1000, tick)           # через 1 секунду функция снимает время
    screen_time.config(text=current_time)           # присваиваем виджету текущее время

def on_click():             # установка времени будильника
    global time_alarm
    time_alarm = entry_time.get().strip()

    mb.showinfo('Включение будильника', f'Будильник включен на {time_alarm}')

def off_click():             # установка времени будильника
    global time_alarm
    time_alarm = ''
    entry_time.delete(0, END)
    pg.mixer.music.stop()
    mb.showwarning('Выключение будильника', f'Будильник выключен')

time_alarm = ''

root = Tk()         # создание окна
root.title('Будильник')        # называем окно      - root - корневое окно
root.config(bg='black')         # формат окна
WIDTH = root.winfo_screenmmwidth()
HEIGHT = root.winfo_screenheight()
X = 400             # размеры окна
Y = 210             # размеры окна

# задаем положение окна
root.geometry(f'{X}x{Y}+{WIDTH // 2 - X // 2}'
              f'+{HEIGHT // 2 - Y // 2 - 25}')  # изменение размера главного окна + позиция вывода окна на мониторе

# создаем элемент в главном окне - Часы
screen_time = Label(root, text='00:00:00', font='Arial 50')         # размещаем в коневом окне root
screen_time.config(bg='black', fg='lime')
screen_time.pack()


# создаем элемент в главном окне ниже часов - окно ввода будущего времени
entry_time = Entry(root, width=10, font='Arial 20', justify=CENTER)            # размещаем в коневом окне root по центру
entry_time.pack()


# создаем кнопку
on = Button(root, text='Включить', font=('Arial', 10), command=on_click)              # размещаем в коневом окне root
on.pack(pady=10)                # pady - отступ по оси Y вниз


off= Button(root, text='Выключить', font=('Arial', 10), command=off_click)              # размещаем в коневом окне root
off.pack()                # pady - есть вверху, здесь не нужно указывать, т.к. виджет располагается ниже предыдущего

tick()

root.mainloop()

