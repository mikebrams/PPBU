from tkinter import *

root = Tk()

lb = Listbox(width=15, height=7)
lb.pack()

lb.insert(0, 'Понедельник')
lb.insert(1, 'Вторник')
lb.insert(2, 'Среда')
lb.insert(3, 'Четверг')
lb.insert(4, 'Пятница')
lb.insert(5, 'Суббота')
lb.insert(6, 'Воскресенье')


root.mainloop()