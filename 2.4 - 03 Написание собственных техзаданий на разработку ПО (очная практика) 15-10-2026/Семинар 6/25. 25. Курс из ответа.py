import json

text = input()
currency = input()

data = json.loads(text)

if data['result'] != 'success':
    print('Сервис не знает эту валюту')
elif currency not in data['rates']:
    print(f'Нет курса для {currency}')
else:
    print(f'1 {data['base_code']} = {data['rates'][currency]:.2f} {currency}')
