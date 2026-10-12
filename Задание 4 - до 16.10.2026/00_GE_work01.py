import tkinter as tk

def paint(event):
    # Рисуем точку (овал) в позиции курсора
    canvas.create_oval(event.x-1, event.y-1, event.x+1, event.y+1, fill='black', width=5)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack()

# Привязываем движение с зажатой кнопкой к функции paint
canvas.bind("<B1-Motion>", paint)

root.mainloop()




import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Рисуем красный овал с чёрным контуром толщиной 2 пикселя
canvas.create_rectangle(50, 5, 250, 200, fill="red", outline="black", width=2)

root.mainloop()



from tkinter import *

def mouse_click(event):
    print(f"Клик мыши на позиции: {event.x}, {event.y}, {event.x_root}, {event.y_root}")

window = Tk()
window.bind("<Button-1>", mouse_click)
window.mainloop()
