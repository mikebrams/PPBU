from tkinter import *
from tkinter import messagebox as mb

def book_seat(seats: dict):
    s = input('Введите место для бронирования (от Б1 до Б9): ')
    try:
        if seats[s] == "свободно":
            seats[s] = 'забронировано'
            print(f'Место {s} успешно забронировано')
        else:
            print(f'Место {s} уже забронировано или не существует.')
    except KeyError:
        print(f'Место {s} не существует')


seats: dict = {f'Б{i}': 'свободно' for i in range(1, 10)}

while True:
    book_seat(seats)
    booking = input('Хотите забронировать еще одно место? (да/нет): ')
    if booking.lower() != 'да':
        break



print('Итоговое состояние бронирования мест.')
for l, n in seats.items():
    print(f'{l}: {n}')