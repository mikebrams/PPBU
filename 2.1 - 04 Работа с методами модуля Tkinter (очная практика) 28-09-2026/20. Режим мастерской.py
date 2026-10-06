from tkinter import *

def turn():
    l_reg.config(text=f'Режим: {reg.get()}')


root = Tk()
root.title('Режим мастерской')
root.geometry('520x420')

focus = 'Фокус'
ideas = 'Идеи'
rest = 'Отдых'

reg = StringVar(value=focus)

rb1 = Radiobutton(root, text='Фокус', variable=reg, value=focus)
rb1.pack(pady=3)

rb2 = Radiobutton(root, text='Идеи', variable=reg, value=ideas)
rb2.pack(pady=3)

rb3 = Radiobutton(root, text='Отдых', variable=reg, value=rest)
rb3.pack(pady=3)


b = Button(root, text='Включить', width=20, bg='SteelBlue', fg='white', command=turn)
b.pack(pady=3)


l_reg = Label(root, text='Режим: не выбран', width=20, bg='#B8F9C9')
l_reg.pack(pady=3)

root.mainloop()
