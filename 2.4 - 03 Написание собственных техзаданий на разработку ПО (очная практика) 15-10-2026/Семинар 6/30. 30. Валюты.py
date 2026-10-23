from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def show_rate():
    curr1 = cb1.get()
    curr2 = cb2.get()
    if not curr1 or not curr2:
        l1.config(text='Выберите обе валюты')
        return
    else:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/' + curr1, timeout=5)
            response.raise_for_status()  # Проверяем, не произошла ли ошибка HTTP
            data = response.json()

            if data['result'] != 'success':
                mb.showerror('Ошибка', 'Сервис не знает эту валюту')
                l1.config(text='Курс не получен')
                return
            else:
                l1.config(text=f'1 {curr1} = {data['rates'][curr2]:.2f} {curr2}')
        except requests.RequestException:
            mb.showerror('Ошибка', 'Сервер недоступен')
            l1.config(text='Курс не получен')
            return


currencies = ['USD', 'EUR', 'RUB', 'CNY', 'KZT']

root = Tk()
root.title('Валюты')
root.geometry('420x260')

Label(text='Из валюты:').pack(pady=5)

cb1 = ttk.Combobox(values=currencies, state='readonly')
cb1.pack(pady=5)

Label(text='В валюту:').pack(pady=5)

cb2 = ttk.Combobox(values=currencies, state='readonly')
cb2.pack(pady=5)

Button(text='Показать курс', command=show_rate).pack(pady=10)

l1 = Label(text='Выберите валюты')
l1.pack(pady=5)

root.mainloop()
