from tkinter import *

def message():
    s = sound.get()
    h = hint.get()

    if s and h:
        msg.config(text=f'Включено: Звук, Подсказки')
    elif s:
        msg.config(text=f'Включено: Звук')
    elif h:
        msg.config(text=f'Включено: Подсказки')
    else:
        msg.config(text=f'Включено: ничего')

root = Tk()
root.title('Уведомления')
root.geometry('520x420')

sound = BooleanVar(root, value=False)
hint = BooleanVar(root, value=False)

sound_box = Checkbutton(root, text="Звук", variable=sound, onvalue=True, offvalue=False)
sound_box.pack(pady=3)

hint_box = Checkbutton(root, text="Подсказки", variable=hint, onvalue=True, offvalue=False)
hint_box.pack(pady=3)

b_apply = Button(text='Применить', command=message)
b_apply.pack(pady=3)

msg = Label(text='Включено: ничего')
msg.pack(pady=3)

root.mainloop()