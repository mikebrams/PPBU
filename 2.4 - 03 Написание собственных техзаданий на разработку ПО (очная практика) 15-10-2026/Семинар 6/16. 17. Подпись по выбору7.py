from tkinter import *

previous = None


def on_select(event):
    global previous
    selection = breeds_list.curselection()
    print(breeds_list.curselection(), 1)
    if not selection:
        l1.config(text="Выберите породу")
        return

    else:
        if selection != previous:
            print(breeds_list.curselection(), 2)
            s = selection[0]
            breed = breeds_list.get(s)
            try:
                l1.config(text=captions[breed])
                print(breeds_list.curselection(), 2==2)
            except KeyError:
                l1.config(text='Подписи нет')
            previous = selection
            print(breeds_list.curselection(), 3)
        else:
            breeds_list.selection_clear(0, END)
            previous = None
            l1.config(text="Выберите породу")
            print(breeds_list.curselection(), 4)


root = Tk()
root.title('Пёсики: подписи')
root.geometry('360x300')

CODES = ["beagle", "pug", "husky", "corgi", "dachshund", "akita", "shiba"]
captions = {"beagle": "Бигль", "pug": "Мопс", "husky": "Хаски", "corgi": "Корги",
            "dachshund": "Такса"}

l1 = Label(text='Выберите породу')
l1.pack()

breeds_list = Listbox()
breeds_list.insert(END, *CODES)
breeds_list.bind('<<ListboxSelect>>', on_select)
breeds_list.pack(pady=10)

root.mainloop()
