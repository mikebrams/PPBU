import json
from tkinter import *
import requests

status_code = int(input())


if 200 <= status_code <= 299:
    print('Успех')
elif status_code == 404:
    print('Не найдено')
elif 400 <= status_code <= 499:
    print('Ошибка в запросе')
elif 500 <= status_code <= 599:
    print('Ошибка сервера')
else:
    print('Другой ответ')

print('raise_for_status: исключение' if status_code >= 400 else 'raise_for_status: молчит')

