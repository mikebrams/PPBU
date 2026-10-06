"""
dict - неупорядоченный набор пар ключ: значение,
в которых ключ уникален и является неизменяемым типом данных
"""

d = {'Pb': 'Свинец', 'Au': 'золото'}

d['Au'] = 'Золото'

print(d)

# метод get
print(d.get('Pb1', 'my item'))

d['Fe'] = 'Железо'
print(d)

# метод setdefault          - запрещает присвоение по существующим ключам
d.setdefault('Fe', '1000')
print(d)

# метод setdefault          - запрещает присвоение по существующим ключам
d.setdefault('1', '1000')
print(d)


# update          - добавление нескольких пар ключ: значение
d.update({ '3': '33', '1': '11'})
print(d)

n = d.pop('Fe')
print(n)
print(d)


nn = d.popitem()        # убирает последнюю добавленную пару
#                       # как бы была добавлена последней 1: 11, но это было обновление старых данных,
                        # а 3: 33 было добавлено непосредственно
print(nn)
print(d)

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

#-----------------------------------------------------------------------------------------
print()
print("-" * 50, '\n')

# Создание словаря
lst = [('Pb', 'Свинец'), ('Au', 'золото')]
dd =dict(lst)
print(dd)

lst = [11, 22, 33]
dd = dict.fromkeys(lst, 0)
print(dd)


dd = {i: i**2 for i in range(10, 20)}
print(dd)

dd = {k: v**2 for k, v in enumerate(range(20))}
print(dd)


a = [1, 2, 3, 4, 5, 7]
b = [1, 2, 3, 4, 5, 6]

dd = {k: v**2 for k, v in zip(a, b)}
print(dd)







