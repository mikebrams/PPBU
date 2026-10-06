from tkinter import *
def delete():
    text.delete(1.0, END)
def insert():
    pushkin = "Это текстовое поле можно очистить с помощью кнопки"
    text.insert(1.0, pushkin)
window = Tk()
text = Text(width=30, height=8, bg="gray", wrap=WORD)
text.pack(side=LEFT)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
b1 = Button(text="Вставка текста", command=insert)
b1.pack(side=LEFT)
b2 = Button(text="Удаление текста", command=delete)
b2.pack(side=LEFT)
window.mainloop()
