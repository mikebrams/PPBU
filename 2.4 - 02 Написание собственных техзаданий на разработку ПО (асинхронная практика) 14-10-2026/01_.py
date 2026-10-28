from tkinter import *

def move_ball(event):
    key = event.keysym
    x1, y1, x2, y2 = canvas.coords(ball)
    if key == "Up":   # Управление только стрелкой вверх
        canvas.move(ball, 0, -20)

window = Tk()
window.title("Игра с шариком")
window.geometry("400x300")

canvas = Canvas(window, width=400, height=300)
canvas.pack()

ball = canvas.create_oval(180, 180, 220, 220, fill="red")

window.bind("<KeyPress>", move_ball)
window.focus_set()

window.mainloop()

