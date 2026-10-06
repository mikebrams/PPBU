from tkinter import *

root = Tk()

kvas = 'квас'
tea = 'чай'
coffee = 'кофе'

drink = StringVar(value=coffee)

m = Label(text='Выбери любимый напиток')
m.pack()

m2 = Label(textvariable=drink, bg='SteelBlue', width=15)
m2.pack()

b1 = Radiobutton(text=kvas, value=kvas, variable=drink)
b1.pack()

b2 = Radiobutton(text=tea, value=tea, variable=drink)
b2.pack()

b3 = Radiobutton(text=coffee, value=coffee, variable=drink)
b3.pack()


root.mainloop()


# import tkinter as tk
# root = tk.Tk()
# root.title("Лаборатория")
#
# status = tk.StringVar(root, value="В пути")
# out = tk.Label(root, textvariable=status)
# out.pack()
# status.set("На месте")
# s = status.get()
#
#
#
# root.mainloop()
