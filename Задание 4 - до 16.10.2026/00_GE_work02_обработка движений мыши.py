# https://younglinux.info/tkinter/event?ysclid=mv4avn2i4b777803216


# from tkinter import *
#
# def b1(event):
#     root.title(f'Левая кнопка мыши')
#
# def b3(event):
#     root.title('Правая кнопка мыши')
#
# def move(event):
#     x = event.x
#     y = event.y
#     s = 'Движение мышью {}x{}'.format(x, y)
#     root.title(s)
#
# root = Tk()
# root.minsize(width=500, height=400)
#
# root.bind('<Button-1>', b1)
# root.bind('<Button-3>', b3)
# root.bind('<Motion>', move)
#
# root.mainloop()
#
# ---------------------------------------------------------------------------------
#
# from tkinter import *
#
# def event_info(event):
#     print(type(event))
#     print(event)
#     print(event.time)
#     print(event.x_root)
#     print(event.y_root)
#
# root = Tk()
# root.bind('a', event_info)
# root.mainloop()

# ---------------------------------------------------------------------------------



# from tkinter import *
#
#
# def enter_leave(event):
#     if event.type == '7':
#         event.widget['text'] = 'In'
#     elif event.type == '8':
#         event.widget['text'] = 'Out'
#
#
# root = Tk()
#
# lab1 = Label(width=20, height=3, bg='white')
# lab1.pack()
# lab1.bind('<Enter>', enter_leave)
# lab1.bind('<Leave>', enter_leave)
#
# lab2 = Label(width=20, height=3, bg='black', fg='white')
# lab2.pack()
# lab2.bind('<Enter>', enter_leave)
# lab2.bind('<Leave>', enter_leave)
# root.mainloop()

# ---------------------------------------------------------------------------------



from tkinter import *

def exit_win(event):
    root.destroy()

def to_label(event):
    t = ent.get()
    lbl.configure(text=t)

def select_all(event):
    def select_all2(widget):
        widget.selection_range(0, END)
        widget.icursor(END)  # курсор в конец
    root.after(10, select_all2, event.widget)

root = Tk()

ent = Entry(width=40)
ent.focus_set()
ent.pack()
lbl = Label(height=3, fg='orange', bg='darkgreen', font='Verdana 24')
lbl.pack(fill=X)

ent.bind('<Return>', to_label)
ent.bind('<Control-a>', select_all)
root.bind('<Control-q>', exit_win)

root.mainloop()