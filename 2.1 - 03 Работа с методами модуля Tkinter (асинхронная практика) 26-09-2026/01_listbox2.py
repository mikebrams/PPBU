from tkinter import *

root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'200x150+{w // 4}+{h // 3}')

lb = Listbox(width=15, height=7)
lb.pack()




week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

for day in week:
    lb.insert(END, day)


root.mainloop()