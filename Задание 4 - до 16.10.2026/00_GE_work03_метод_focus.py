from tkinter import *

def next_widget(event):
    event.widget.tk_focusNext().focus()

window = Tk()
Entry().pack()
Entry().pack()


# entry1 = Entry()
# entry1.bind("<Tab>", next_widget)
window.bind("<Tab>", next_widget)

window.mainloop()     #Bind_04.py




