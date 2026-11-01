from tkinter import *

CODES = ["beagle", "pug", "husky", "corgi", "dachshund", "akita", "shiba"]
captions = {
    "beagle": "Бигль",
    "pug": "Мопс",
    "husky": "Хаски",
    "corgi": "Корги",
    "dachshund": "Такса"
}


def on_select(event):
    selection = breeds_list.curselection()

    if not selection:
        caption.config(text="Выберите породу")
    else:
        code = breeds_list.get(selection[0])
        caption.config(text=captions.get(code, "Подписи нет"))


window = Tk()
window.title("Пёсики: подписи")
window.geometry("360x300")

breeds_list = Listbox()
breeds_list.pack(pady=10)

for code in CODES:
    breeds_list.insert(END, code)

breeds_list.bind("<<ListboxSelect>>", on_select)

caption = Label(text="Выберите породу")
caption.pack()

window.mainloop()