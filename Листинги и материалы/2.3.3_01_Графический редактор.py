from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk


def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + 5, y + 5, fill=pen_color, outline=pen_color)


def load_image():
    file_path = fd.askopenfilename(filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
    if file_path:
        image = Image.open(file_path)
        image = image.resize((600, 400))
        image_tk = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=NW, image=image_tk)
        canvas.image = image_tk


window = Tk()
window.title("Рисование на холсте")

pen_color = "red"
canvas = Canvas(window, width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

colors = ["red", "green", "blue", "black"]
for color in colors:
    lbl = Label(window, text="", bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<Button-1>", lambda e, c=color: globals().update(pen_color=c))

Button(window, text="Загрузить изображение", command=load_image).pack()
window.mainloop()




