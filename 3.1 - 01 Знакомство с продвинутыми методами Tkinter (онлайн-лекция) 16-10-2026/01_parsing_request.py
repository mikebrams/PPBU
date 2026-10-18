import requests
from bs4 import BeautifulSoup

""" https://www.hse.ru/staff/allat/"""


def get_main(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('h1', class_='person-caption').text

    pos = soup.find('span', class_='person-appointment-title').text.strip()[:-1]

    langs = soup.find('dt', class_='b').find_all('dd')
    res = (name, pos)
    print(res)

    for l in langs:
        print(l.text)


pull_address = ('https://www.hse.ru/staff/allat/',
                'https://www.hse.ru/org/persons/135897',
                'https://www.hse.ru/org/persons/63890353')

for add in pull_address:
    get_main(add)