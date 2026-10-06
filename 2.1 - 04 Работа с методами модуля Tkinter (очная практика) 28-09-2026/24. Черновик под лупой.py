from tkinter import *

def check_len():
    text_get = text.get('1.0', 'end-1c')
    if text_get:
        msg.config(text=f'Символов: {len(text_get)} | Строк: {text_get.count('\n') + 1}')

def remove():
    if text:
        text.delete(1.0, END)
        msg.config(text=f'Символов: 0 | Строк: 0')
1

root = Tk()
root.title('Черновик под лупой')
root.geometry('620x500')

text = Text(root, height=16, font='Arial 12')
text.pack(fill='x', padx=20, pady=10)

frame = Frame()
frame.pack()

check = Button(frame, text='Проверить', bg='RoyalBlue', fg='white', width=16, font='Arial 14 bold', command=check_len)
check.pack(side=LEFT, padx=6, pady=5)

remove = Button(frame, text='Очистить', bg='RoyalBlue', fg='white', width=16, font='Arial 14 bold', command=remove)
remove.pack(side=LEFT, padx=6, pady=5)

msg = Label(root, text='Символов: 0 | Строк: 0', bg='#ECFDF1', width=24, font='Arial 14 bold')
msg.pack(pady=15)

root.mainloop()