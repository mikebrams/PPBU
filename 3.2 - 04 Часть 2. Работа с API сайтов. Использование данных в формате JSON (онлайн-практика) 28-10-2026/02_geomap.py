from Scripts.bottle import response
from opencage.geocoder import OpenCageGeocode
from tkinter import *
from translate import Translator
import webbrowser
import requests

translator = Translator(from_lang='en', to_lang='ru')


def get_weather(lat, lon):
    try:
        response = requests.get(f'https://api.open-meteo.com/v1/forecast'
                                f'?latitude={lat}&longitude={lon}'
                                f'&current_weather=true')
        # response.raise_for_status()
        weather_data = response.json()
        current_weather = weather_data['current_weather']
        return current_weather
    except Exception as e:
        return f'Ошибка при получении погоды: {e}'


def show_weather():
    current_weather = get_weather(lat, lon)
    weather_window = Toplevel(root)
    weather_window.title('Текущая погода')
    weather_window.geometry('200x100+300+200')
    if isinstance(current_weather, str):
        label = Label(weather_window, text=current_weather)
    else:
        temperature = current_weather['temperature']
        windspeed = current_weather['windspeed']
        weather_text = (f'Температура {temperature} ℃,\n'
                        f'Скорость ветра {windspeed} км/ч')
        label = Label(weather_window, text=weather_text)
    label.pack()

def get_coordinates(city, key):
    global lat, lon
    try:
        geocoder = OpenCageGeocode(key)
        query = city
        results = geocoder.geocode(query)
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lat_full = results[0]['geometry']['lat']
            lon = round(results[0]['geometry']['lng'], 2)
            lng_full = results[0]['geometry']['lng']
            country = results[0]['components']['country']
            region = results[0]['components']['state']
            osm_url = f'https://www.openstreetmap.org/?mlat={lat_full}&mlon={lng_full}'
            return {
                "coordinates": f'Широта: {lat_full:.2f}, Долгота: {lng_full:.2f},'
                               f'\nСтрана: {translator.translate(country)}, Регион: {translator.translate(region)}',
                "map_url": osm_url
            }
        else:
            return {"ccordinates": 'Город не найден', "map_url": None}
    except Exception as e:
        return f'Ошибка: {e}'


def show_coordinates(event=None):
    global map_url
    city = entry.get().strip()
    result = get_coordinates(city, key)
    label['text'] = result["coordinates"]

    map_url = result['map_url']


def show_map(event=None):
    if map_url:
        webbrowser.open(map_url)


map_url = None
lat = None
lon = None
key = '96112fb6d80d4059ae9dabea94898600'

root = Tk()
root.title('Поиск координат города')
root.geometry('400x150')

frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack(pady=(15, 0))


entry = Entry(frame1)
entry.pack(pady=(10, 0))
entry.bind('<Return>', show_coordinates)

label = Label(frame1, text='Введите город')
label.pack()

btn = Button(frame2, text='Получить координаты', command=show_coordinates)
btn.grid(row=0, column=0, padx=5)

map_btn = Button(frame2, text='Показать на карте', command=show_map)
map_btn.grid(row=0, column=1, padx=5)

weather_btn = Button(frame2, text='Показать погоду', command=show_weather)
weather_btn.grid(row=0, column=2, padx=5)

root.mainloop()
