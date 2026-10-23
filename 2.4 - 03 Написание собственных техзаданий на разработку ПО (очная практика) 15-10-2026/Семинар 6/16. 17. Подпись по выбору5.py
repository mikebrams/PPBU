from tkinter import *

previous = None

def on_select(event):
    global previous
    selection = breeds_list.curselection()

    if not selection:
        l1.config(text="Выберите породу")
        return

    else:
        breed_input = breeds_list.curselection()
        print(breed_input)
        if breed_input == previous:
            breeds_list.selection_clear(0, END)
            l1.config(text="Выберите породу")
            previous = None
        else:
            s = breed_input[0]
            breed = breeds_list.get(s)
            try:
                l1.config(text=captions[breed])
            except KeyError:
                l1.config(text='Подписи нет')
            previous = breed_input

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

