from tkinter import *
from tkinter import messagebox as mb


def book_seat():
    s = seat_entry.get()
    try:
        if seats[s] == "свободно":
            seats[s] = 'забронировано'
            update_canvas()
            mb.showinfo('Успех', f'Место {s} успешно забронировано')
        else:
            mb.showinfo('Ошибка', f'Место {s} уже забронировано или не существует.')
    except KeyError:
        mb.showerror('Ошибка', f'Место {s} не существует')


def update_canvas():
    canvas.delete('all')
    for i, (seat, status) in enumerate(seats.items()):
        x = i * 40 + 20
        y = 20
        color = 'green' if status == 'свободно' else 'red'
        canvas.create_rectangle(x, y, x + 30, y + 30, fill=color)
        canvas.create_text(x+15, y+15, text=seat)


root = Tk()
root.title('Бронирование мест')
root.geometry('400x200')

canvas = Canvas(width=400, height=60)
canvas.pack(pady=10)

seats: dict = {f'Б{i}': 'свободно' for i in range(1, 10)}
update_canvas()

seat_entry = Entry()
seat_entry.pack(pady=10)

Button(text='Забронировать место', command=book_seat).pack(pady=10)

root.mainloop()

#
# while True:
#     book_seat(seats)
#     booking = input('Хотите забронировать еще одно место? (да/нет): ')
#     if booking.lower() != 'да':
#         break


print('Итоговое состояние бронирования мест.')
for l, n in seats.items():
    print(f'{l}: {n}')
