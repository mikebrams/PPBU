import requests
import pprint

day = input('Введите дату получения котировок в формате ДД-ММ-ГГГГ: ')
# на сайте данные предоставлены за последний календарный год с момента запроса
# Public API users are limited to querying historical data within the past 365 days.
# Upgrade to a paid plan to enjoy full historical data access: https://www.coingecko.com/en/api/pricing

p = pprint.PrettyPrinter(indent=4)
result = requests.get(f'https://pro-api.coinmarketcap.com/public-api/v3/bitcoin/listings/latest/')
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
# https://coinmarketcap.com/api/
# https://pro-api.coinmarketcap.com/public-api/v3/bitcoin/listings/latest
coinmarketca = {   'status': {   'credit_count': 0,
                  'elapsed': '0',
                  'error_code': '500',
                  'error_message': 'The system is busy, please try again '
                                   'later!',
                  'timestamp': '2026-10-27T20:27:55.676Z'}}






crypto = {
    'BTC': ('Bitcoin', 'bitcoin'),
    'ETH': ('Ethereum', 'ethereum'),
    'STX': ('Stacks', 'blockstack'),
    'USDT': ('Tether', 'tether')
}
