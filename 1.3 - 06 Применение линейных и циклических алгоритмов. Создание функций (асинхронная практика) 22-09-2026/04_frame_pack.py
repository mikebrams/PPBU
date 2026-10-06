from tkinter import *



window = Tk()

frame_top = Frame(window)
# фреймы для упорядочивания виджетов
frame_bottom = Frame(window)

frame_top.pack()            # разместить фреймы
frame_bottom.pack(side=BOTTOM)


metka1 = Label(frame_top, text='Метка 1', bg='red')
metka1.pack(side=LEFT)       # размещение метки

metka2 = Label(frame_top, text='Метка 2', bg='yellow')
metka2.pack(side=LEFT)

metka3 = Label(frame_top, text='Метка 3', bg='green')
metka3.pack(side=LEFT)

metka4 = Label(frame_bottom,text='Метка 4', bg='blue')
metka4.pack(side=LEFT)

metka5 = Label(frame_bottom,text='Метка 5', bg='gray')
metka5.pack(side=LEFT)

metka6 = Label(frame_bottom,text='Метка 6', bg='salmon')
metka6.pack(side=LEFT)


window.mainloop()

