captions = {"beagle": "Бигль", "pug": "Мопс", "husky": "Хаски", "corgi": "Корги", "dachshund": "Такса"}

breed = input()
print(captions.get(breed, 'Подписи нет'))