from tkinter import *
import random
import time
from tkinter import messagebox as mb

def move_ball(event):
    key = event.keysym
    x1, y1, x2, y2 = canvas.coords(ball)
    if key == "Up" and y1 > 0:
        canvas.move(ball, 0, -20)
    elif key == "Down" and y2 < 300:
        canvas.move(ball, 0, 20)
    elif key == "Left" and x1 > 0:
        canvas.move(ball, -20, 0)
    elif key == "Right" and x2 < 400:
        canvas.move(ball, 20, 0)
    check_collision()

def check_collision():
    b = canvas.coords(ball) # список координат "углов" шарика
    s = canvas.coords(square) # список координат углов квадрата
    if b[2] > s[0] and b[0] < s[2] and b[3] > s[1] and b[1] < s[3]:
        move_square()
        update_score()

def move_square():
    x1, y1 = random.randint(0, 380), random.randint(0, 280)
    x2, y2 = x1 + 20, y1 + 20
    canvas.coords(square, x1, y1, x2, y2)

def update_score():
    global score, start_time
    score += 1
    score_label.config(text=f'Счет: {score}')
    if score >= 10:
        end_time = time.time()
        if end_time - start_time <= 20:
            mb.showinfo('Игра окончена!', f'Победа! Вы прошли игру за {end_time - start_time:.1f} сек.')
        else:
            mb.showinfo('Вы проиграли!', 'Время вышло!')
        if mb.askyesno("Игра окончена", 'Хотите сыграть еще раз?'):
            start_game()
        else:
            root.destroy()

def start_game():
    global score, start_time
    score = 0
    score_label.config(text=f'Счет: {score}')
    start_time = time.time()
    move_square()

root = Tk()
root.title('Игра с шариком')
root.geometry('400x330')

canvas = Canvas(width=400, height=300)
canvas.pack()

ball = canvas.create_oval(180, 180, 220, 220, fill='red')
square = canvas.create_rectangle(150, 150, 170, 170, fill='blue')

score = 0
start_time = time.time()

score_label = Label(text=f'Счет: {score}')
score_label.pack()

root.bind("<KeyPress>", move_ball)
root.focus_set()

root.mainloop()