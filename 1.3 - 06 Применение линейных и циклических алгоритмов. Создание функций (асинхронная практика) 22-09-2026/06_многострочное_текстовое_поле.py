from tkinter import *

def read():
    t = text.get(1.0, END)
    print(t)
    text.delete(1.0, END)


window = Tk()
window.title('Title')

# создание многострочного текстового поля
text = Text(width=30, height=8, bg='gray', fg='white', font='Arial 12 bold', wrap=WORD)
text.pack(side=LEFT)
sample_text = "Это очень длинный текст, который должен переноситься по словам, а не по символам."
text.insert("1.0", sample_text)


# ttt = Entry(text='fgbsgfbsfgsfng')
# ttt.pack()

scroll = Scrollbar(command=text.yview)        # создание полосы прокрутки
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

b = Button(text='ввод', command=read)
b.pack()

b2 = Button(text='вставка')
b2.pack()


window.mainloop()