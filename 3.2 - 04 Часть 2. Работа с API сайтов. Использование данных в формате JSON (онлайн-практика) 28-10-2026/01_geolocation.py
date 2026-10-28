from opencage.geocoder import OpenCageGeocode
import pprint
from tkinter import *
from tkinter import messagebox as mb
from translate import Translator
import webbrowser

translator = Translator(from_lang='en', to_lang='ru')
st = 'Russia'
res = translator.translate(st)
print(res)


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        query = city
        results = geocoder.geocode(query)
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(results)
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return (f'Широта: {lat}, Долгота: {lng}\n'
                        f'Страна: {translator.translate(country)},\nРегион: {translator.translate(region)}')
            else:
                return (f'Широта: {lat}, Долгота: {lng}\n'
                        f'Страна: {translator.translate(country)}')
        else:
            return 'Город не найден'
    except Exception as e:
        return f'Ошибка: {e}'


def show_coordinates(event=None):
    city = entry.get().strip()
    coordinates = get_coordinates(city, key)
    label.config(text=coordinates)


key = '96112fb6d80d4059ae9dabea94898600'
# city = 'Ялта'
# coordinates = get_coordinates(city, key)
# print(coordinates)

root = Tk()
root.title('Поиск координат города')
root.geometry('400x200')

entry = Entry()
entry.pack(pady=(10, 20))
entry.bind('<Return>', show_coordinates)

label = Label(text='Введите город')
label.pack()

root.mainloop()
