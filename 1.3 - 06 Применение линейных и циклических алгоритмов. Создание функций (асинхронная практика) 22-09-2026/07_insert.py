from tkinter import *

def delete():
    text.delete(1.0, END)

def insert():
    pushkin = ('Я помню чудное мгновенье: Передо мной явилась ты, \
               Как мимолетное виденье, Как гений чистой красоты. \
               В томленьях грусти безнадежной, В тревогах шумной суеты, \
               Звучал мне долго голос нежный И снились милые черты.')
    T = text.insert(1.0, pushkin)

window = Tk()
window.title('Title')

# создание многострочного текстового поля
text = Text(width=30, height=8, bg='gray', fg='white', font='Arial 12 bold', wrap=WORD)
text.pack(side=LEFT)

scroll = Scrollbar(command=text.yview)        # создание полосы прокрутки
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

b = Button(text='Вставка текста', command=insert)
b.pack()


b2 = Button(text='Удаление текста', command=delete)
b2.pack(side=LEFT)


window.mainloop()