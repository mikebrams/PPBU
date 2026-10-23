from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import json
import pprint

p = pprint.PrettyPrinter(indent=4)
result = requests.get('https://open.er-api.com/v6/latest/USD')
data1 = result.json()
p.pprint(data1)

data = json.loads(result.text)
p.pprint(data)
print(data==data1)


def update_currency_label(event):
    code = combobox.get()
    name = currencies_dict[code]
    currency_label.config(text=name)


def exchange():
    # code = entry.get().strip().upper()
    code = combobox.get()
    try:
        response = requests.get('https://open.er-api.com/v6/latest/USD')
        response.raise_for_status()
        data = response.json()
        if code in data['rates']:
            exchange_rate = data['rates'][code]
            mb.showinfo('Курс обмена',
                        f'Курс к USD: {exchange_rate:.1f} {code} за 1 USD')
        else:
            mb.showerror('Ошибка', f'Валюта не найдена')
    except Exception as err:
        mb.showerror('Ошибка', err)


currencies_dict = {'AED': 'Дирхам ОАЭ',
                   'AMD': 'Армянских драмов',
                   'AUD': 'Австралийский доллар',
                   'AZN': 'Азербайджанский манат',
                   'BDT': 'Так',
                   'BHD': 'Бахрейнский динар',
                   'BOB': 'Боливиано',
                   'BRL': 'Бразильский реал',
                   'BYN': 'Белорусский рубль',
                   'CAD': 'Канадский доллар',
                   'CHF': 'Швейцарский франк',
                   'CNY': 'Юань',
                   'CUP': 'Кубинских песо',
                   'CZK': 'Чешских крон',
                   'DKK': 'Датская крона',
                   'DZD': 'Алжирских динаров',
                   'EGP': 'Египетских фунтов',
                   'ETB': 'Эфиопских быров',
                   'EUR': 'Евро',
                   'GBP': 'Фунт стерлингов',
                   'GEL': 'Лари',
                   'HKD': 'Гонконгский доллар',
                   'HUF': 'Форинтов',
                   'IDR': 'Рупий',
                   'INR': 'Индийских рупий',
                   'IRR': 'Иранских риалов',
                   'JPY': 'Иен',
                   'KGS': 'Сомов',
                   'KRW': 'Вон',
                   'KZT': 'Тенге',
                   'MDL': 'Молдавских леев',
                   'MMK': 'Кьятов',
                   'MNT': 'Тугриков',
                   'NGN': 'Найр',
                   'NOK': 'Норвежских крон',
                   'NZD': 'Новозеландский доллар',
                   'OMR': 'Оманский риал',
                   'PLN': 'Злотый',
                   'QAR': 'Катарский риал',
                   'RON': 'Румынский лей',
                   'RSD': 'Сербских динаров',
                   'SAR': 'Саудовский риял',
                   'SEK': 'Шведских крон',
                   'SGD': 'Сингапурский доллар',
                   'THB': 'Батов',
                   'TJS': 'Сомони',
                   'TMT': 'Новый туркменский манат',
                   'TRY': 'Турецких лир',
                   'UAH': 'Гривен',
                   'USD': 'Доллар США',
                   'UZS': 'Узбекских сумов',
                   'VND': 'Донгов',
                   'ZAR': 'Рэндов'}

currencies = {'EUR': 'Евро',
              'JPY': 'Иен',
              'RUB': 'Российский рубль'}
root = Tk()
root.title('Курс обмена валют к USD')
root.geometry('360x180')

Label(root, text='Введите код валюты').pack(pady=10, padx=10)
popular_currencies = ['EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF',
                      'CNY', 'RUB', 'KZT', 'UZS']
popular_currencies.sort()
combobox = ttk.Combobox(root, values=list(currencies_dict.keys()), state='readonly')
combobox.pack(padx=10, pady=10)
combobox.bind('<<ComboboxSelected>>', update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

# entry = Entry(root)
# entry.pack()

Button(text='Получить курс обмена к USD', command=exchange).pack(pady=10, padx=10)

root.mainloop()


