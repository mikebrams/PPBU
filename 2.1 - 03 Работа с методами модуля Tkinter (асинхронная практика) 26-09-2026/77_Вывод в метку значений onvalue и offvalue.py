from tkinter import *

def show():
    m['text'] = " | {} | {} |".format(v1.get(), v2.get())
window=Tk()

v1 = BooleanVar()
v1.set(False)
c1 = Checkbutton(text="First", variable=v1,
                onvalue=True, offvalue=False, command=show)
c1.pack()
v2 = IntVar()
v2.set(0)
c2 = Checkbutton(text="Second", variable=v2,
                onvalue=1, offvalue=0, command=show)
c2.pack()
m = Label(width=15, height=3, bg="lightgrey")
m.pack()
window.mainloop()
