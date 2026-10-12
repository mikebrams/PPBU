from tkinter import *
from tkinter import messagebox as mb


def add_item():
    if s.get() == "0":
        # Добавление имени
        l1.insert(END, e.get())
        e.delete(0, END)
    else:
        # Добавление телефона после проверки
        if validate_phone():
            l2.insert(END, e.get())
            e.delete(0, END)


def del1_item():
    l1.delete(ANCHOR)


def del2_item():
    l2.delete(ANCHOR)


def save():
    try:
        with open('phones.txt', 'w') as f:
            for i in range(l1.size()):
                f.write(f"{l1.get(i)} : {l2.get(i)}\n")
        mb.showinfo("Сохранение", "Контакты успешно сохранены.")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка при сохранении: {e}")


def load():
    try:
        with open('phones.txt', 'r') as f:
            l1.delete(0, END)  # Очищаем списки перед загрузкой
            l2.delete(0, END)
            for line in f:
                name, _, phone = line.partition(" : ")
                l1.insert(END, name.strip())
                l2.insert(END, phone.strip())
        mb.showinfo("Загрузка", "Контакты успешно загружены.")
    except FileNotFoundError:
        mb.showerror("Ошибка", "Файл не найден.")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка при загрузке: {e}")


def validate_phone():
    phone_number = e.get()
    if len(phone_number) == 10 and phone_number.isdigit() and phone_number.startswith('9'):
        # Проверка пройдена
        mb.showinfo("Операция выполнена", "Номер успешно добавлен")
        return True
    else:
        # Проверка не пройдена
        mb.showerror("Ошибка", "Номер должен быть 10-значным, состоять только из цифр и начинаться с 9")
        e.delete(0, END)
        return False


window = Tk()
s = StringVar(value=0)
f1 = Frame()
f1.pack(side=LEFT)
m1 = Label(f1, text="Имя")
m1.pack()
l1 = Listbox(f1)
l1.pack()
scroll = Scrollbar(command=l1.yview)
scroll.pack(side=LEFT, fill=Y)
l1.config(yscrollcommand=scroll.set)

f2 = Frame()
f2.pack(side=LEFT)
m2 = Label(f2, text="Телефон")
m2.pack()
l2 = Listbox(f2)
l2.pack()
scroll = Scrollbar(command=l2.yview)
scroll.pack(side=LEFT, fill=Y)
l2.config(yscrollcommand=scroll.set)

f3 = Frame()
f3.pack(side=LEFT)
radio1 = Radiobutton(f3, text="Имя", value=0, variable=s)
radio1.pack()
radio2 = Radiobutton(f3, text="Телефон", value=1, variable=s)
radio2.pack()
e = Entry(f3)
e.pack()

b1 = Button(f3, text="Добавить", command=add_item)
b1.pack(fill=X)
b2 = Button(f3, text="Удалить имя", command=del1_item)
b2.pack(fill=X)
b3 = Button(f3, text="Удалить телефон", command=del2_item)
b3.pack(fill=X)
b4 = Button(f3, text="Сохранить", command=save)
b4.pack(fill=X)
b5 = Button(f3, text="Загрузить", command=load)
b5.pack(fill=X)

window.mainloop()
