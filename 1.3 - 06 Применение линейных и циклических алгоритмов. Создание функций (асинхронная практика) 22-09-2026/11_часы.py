from tkinter import *
import time


def tick():
    t = time.strftime('%H:%M:%S')
    m.config(text=t)
    m.after(1000, tick)               # задержка программы

root = Tk()
root.title('Часы')
root.config(bg='SteelBlue')
root.geometry('320x150')

m = Label(font=('Verdana', 24, 'bold'), bg='SteelBlue', fg='Wheat')
m.pack(pady='5')
tick()



root.mainloop()

