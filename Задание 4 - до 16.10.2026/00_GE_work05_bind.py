from tkinter import *
from tkinter import ttk

clicks = 0

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")


def clicked(event):
    global clicks
    clicks = clicks + 1
    btn["text"] = f"{clicks} Clicks"


btn = ttk.Button(text="Click")
btn.pack(anchor=CENTER, expand=1)

# привязка события к кнопкам ttk.Button
root.bind_class("TButton", "<Double-ButtonPress-1>", clicked)

root.mainloop()