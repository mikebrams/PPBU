import requests
import pprint

day = input('Введите дату получения котировок в формате ДД-ММ-ГГГГ: ')
# на сайте данные предоставлены за последний календарный год с момента запроса
# Public API users are limited to querying historical data within the past 365 days.
# Upgrade to a paid plan to enjoy full historical data access: https://www.coingecko.com/en/api/pricing

p = pprint.PrettyPrinter(indent=4)
result = requests.get(f'https://pro-api.coinmarketcap.com/public-api/v2/simple/price?symbol=BNB&convert=USD')
# result = requests.get(f'https://api.coingecko.com/api/v3/coins/tether/history?date={day}')
# result = requests.get(f'https://api.coingecko.com/api/v3/coins/blockstack/history?date={day}')
# result = requests.get(f'https://api.coingecko.com/api/v3/coins/bitcoin/history?date={day}')
# result = requests.get('https://api.coingecko.com/api/v3/coins/ethereum/history?date={day}')
data1 = result.json()
p.pprint(data1)

# bitcoin
# ETH: ethereum
# добавить возможность выбора до 5 валют и получения по ним информации
# добавить график: цена, рыночная капитализация, объем
# сохранение

# https://www.binance.com/ru/markets/overview
# платный ключ
# https://finance.yahoo.com/markets/crypto/all/         - нет API
# https://www.coinlore.com/cryptocurrency-data-api


# ????????? - не проверено - https://ru.investing.com/crypto
# ????????? - не проверено - https://www.okx.com/ru-eu/okx-api?ysclid=mvsijozqrq782611449
# запрос в поиске - открытые api для криптовалют, открытые api предоставляющие курсы криптовалют

# https://coinmarketcap.com/api/
# https://pro-api.coinmarketcap.com/public-api/v3/bitcoin/listings/latest
# https://pro-api.coinmarketcap.com/public-api/v2/simple/price?symbol=BNB&convert=USD
coinmarketcap = {'data': [{'id': 1839,
                          'name': 'BNB',
                          'quotes': [{'price': 751.0440590638909, 'symbol': 'USD'}],
                          'slug': 'bnb',
                          'symbol': 'BNB'}],
                'status': {'credit_count': 1,
                           'elapsed': 2,
                           'error_code': '0',
                           'error_message': '',
                           'timestamp': '2026-10-28T19:19:08.411Z'}}

"""
Создайте приложение с графическим интерфейсом на языке Python, которое будет отображать
текущие курсы популярных криптовалют к доллару США, используя данные https://coinmarketcap.com/api/
"""

crypto = {
    'BTC': ('Bitcoin', 'bitcoin'),
    'ETH': ('Ethereum', 'ethereum'),
    'STX': ('Stacks', 'blockstack'),
    'USDT': ('Tether', 'tether')
}
