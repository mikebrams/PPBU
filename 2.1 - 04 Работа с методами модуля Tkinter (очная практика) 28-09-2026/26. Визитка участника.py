from tkinter import *


def make_card():
    name_get = name.get().strip()
    project_get = project.get().strip()
    connection = vch1.get()

    if not name_get or not project_get:
        msg.config(text='Ошибка: заполните имя и проект')
    else:
        msg.config(text=f'{name_get} / {project_get} / связь: {connection}')


root = Tk()
root.title('Визитка участника')
root.geometry('620x520')

vch1 = StringVar()
vch1.set('открыта')

frame = Frame(root)
frame.pack()

Label(frame, text='Имя', height=1).grid(row=0, sticky='w', pady=2)

name = Entry(frame, width=50)
name.grid(row=1, sticky='w', pady=3)

Label(frame, text='Проект', height=1).grid(row=2, sticky='w', pady=2)

project = Entry(frame, width=50)
project.grid(row=3, sticky='w', pady=3)


cb1 = Checkbutton(frame, text='Открыт к сообщениям', height=2, variable=vch1, onvalue='открыта', offvalue='закрыта')
cb1.grid(row=4, sticky='w')


card = Button(frame, text='Собрать карточку', bg='RoyalBlue', fg='white', font='Arial 10 bold', height=1, command=make_card)
card.grid(row=5, sticky='we', pady=3)

msg = Label(frame, text='Карточка не создана', bg='#ECFDF1', font='Arial 10 bold', height=1)
msg.grid(row=6, sticky='we', pady=3)


root.mainloop()

# form = Frame(root)
# form.pack(padx=12, pady=12)
# Label(form, text="Имя").grid(row=0, column=0)
# name = Entry(form)
# name.grid(row=0, column=1)
