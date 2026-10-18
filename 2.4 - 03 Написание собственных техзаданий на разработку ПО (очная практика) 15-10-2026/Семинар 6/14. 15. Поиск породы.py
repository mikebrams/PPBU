from tkinter import *

def search():

    found = []

    prompt = e1.get().lower().strip()
    if prompt:

        for breed in BREEDS:
            if prompt in breed:
                found.append(breed)
        if found:
            l1.config(text=f'Найдено: {len(found)}')
            breeds_list.delete(0, END)
            breeds_list.insert(END, *found)

        else:
            breeds_list.delete(0, END)
            l1.config(text='Ничего не найдено')
    if not prompt:
        l1.config(text=f'Найдено: {len(BREEDS)}')
        breeds_list.delete(0, END)
        breeds_list.insert(END, *BREEDS)


def select():

    selected = breeds_list.curselection()

    if selected:
        res = breeds_list.get(selected[0])
        l1.config(text=f'Выбрано: {res}')
    else:
        l1.config(text='Сначала выберите породу')

root = Tk()
root.title('Пёсики: поиск')
root.geometry('400x380')

Label(text='Поиск:').pack()

e1 = Entry(root)
e1.pack()

b = Button(text='Найти', command=search)
b.pack()

BREEDS = ["beagle", "bulldog", "husky", "hound", "labrador", "pug", "poodle", "boxer"]

breeds_list = Listbox(root, height=8)
breeds_list.insert(END, *BREEDS)
breeds_list.pack()

b2 = Button(text='Показать выбранную', command=select)
b2.pack()


l1 = Label(text='Порода не выбрана')
l1.pack()

root.mainloop()

