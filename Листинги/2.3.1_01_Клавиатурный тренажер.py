import tkinter as tk
import time

def start():
    global t, i
    t = time.time()
    i = 0
    update_label(phrase[i])
    window.bind("<Key>", check)

def check(event):
    global i
    if event.char == phrase[i]:
        i += 1
        if i >= len(phrase):
            finish()
        else:
            update_label(phrase[i])
    else:
        update_label(f"Ошибка! Ожидалась буква '{phrase[i]}', нажмите любую клавишу для продолжения")
        window.bind("<Key>", continue_after_error)

def continue_after_error(event):
    update_label(phrase[i])
    window.bind("<Key>", check)

def finish():
    elapsed = time.time() - t
    time_allowed = len(phrase)
    if elapsed <= time_allowed:
        update_label(f"Вы победили! Время: {elapsed:.2f} сек.")
    else:
        update_label(f"Время истекло! Затрачено {elapsed:.2f} сек. Разрешенное время: {time_allowed} сек.")

def update_label(text):
    label.config(text=text)

phrase = "quickbrownfox"
i = 0
t = None

window = tk.Tk()
window.title("Клавиатурный тренажер")
window.geometry("900x100")


label = tk.Label(window, font=("Helvetica", 24))
label.pack()

start()
window.mainloop()
