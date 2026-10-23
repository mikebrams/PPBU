from tkinter import *

previous = None

def on_select(event):
    global previous
    selection = breeds_list.curselection()

    if selection == previous:
        # print(selection, 1)
        breeds_list.selection_clear(selection)
        l1.config(text="Выберите породу")
        previous = None
    else:
        if not selection:
            l1.config(text="Выберите породу")
            return
        else:
            # print(selection, 2)
            s = selection[0]
            breed = breeds_list.get(s)
            try:
                l1.config(text=captions[breed])
            except KeyError:
                l1.config(text='Подписи нет')
            previous = selection


root = Tk()
root.title('Пёсики: подписи')
root.geometry('360x300')

CODES = ["beagle", "pug", "husky", "corgi", "dachshund", "akita", "shiba"]
captions = {"beagle": "Бигль", "pug": "Мопс", "husky": "Хаски", "corgi": "Корги", "dachshund": "Такса"}

l1 = Label(text='Выберите породу')
l1.pack()

breeds_list = Listbox()
breeds_list.insert(END, *CODES)
breeds_list.bind('<<ListboxSelect>>', on_select)
breeds_list.pack(pady=10)

root.mainloop()

