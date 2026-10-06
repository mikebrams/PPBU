from tkinter import *
import time


def tick():
    t = time.strftime('%H:%M:%S')
    m.config(text=t)
    m.after(1000, tick)               # задержка программы


def bg_color():
    m.config(bg=v_bg.get())

def fg_color():
    m.config(fg=v_fg.get())

def font():
    m.config(font=v_font.get())

def height_m():
    m.config(height=v_height.get())


root = Tk()
root.title('Часы')
# root.config(bg='SteelBlue')
# root.geometry('320x150')

# m = Label(font=('Verdana', 24, 'bold'), bg='SteelBlue', fg='Wheat')
m = Label(font=('Verdana', 16, 'bold'), bg='lightblue', fg='black', height=1)
m.pack(pady='5')
tick()

v_bg = StringVar()
v_bg.set('lightblue')
v_fg = StringVar()
v_fg.set('black')
v_font = StringVar()
v_font.set('Verdana 16')
v_height = IntVar()
v_height.set(1)

c1 = Checkbutton(text='Переключатель цвета фона', variable=v_bg, onvalue='salmon', offvalue='lightblue', command=bg_color)
c1.pack()
c2 = Checkbutton(text='Переключатель цвета текста', variable=v_fg, onvalue='white', offvalue='black', command=fg_color)
c2.pack()
c3 = Checkbutton(text='Переключатель шрифта', variable=v_font, onvalue='Arial 16', offvalue='Verdana 16', command=font)
c3.pack()
c4 = Checkbutton(text='Переключатель высоты метки', variable=v_height, onvalue=3, offvalue=1, command=height_m)
c4.pack()


root.mainloop()
