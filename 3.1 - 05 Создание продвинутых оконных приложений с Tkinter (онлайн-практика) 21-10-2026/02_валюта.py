from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import json
import pprint

# p = pprint.PrettyPrinter(indent=4)
# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
# p.pprint(data)


def exchange():
    code = entry.get().strip().upper()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()

            data = response.json()
            print(data)

            if code in data['rates']:
                exchange_rate = data['rates'][code]
                mb.showinfo('Курс обмена',
                            f'Курс к USD: {exchange_rate:.1f} {code} за 1 USD')
            else:
                mb.showerror('Ошибка', f'Валюта не найдена')
        except Exception as err:
            mb.showerror('Ошибка', err)
    else:
        mb.showwarning('Внимание', 'Введите код валюты')


root = Tk()
root.title('Курс обмена валют к USD')
root.geometry('360x180')

Label(root, text='Введите код валюты').pack(pady=10, padx=10)

entry = Entry(root)
entry.pack()

Button(text='Получить курс обмена к USD', command=exchange).pack(pady=10, padx=10)

root.mainloop()
