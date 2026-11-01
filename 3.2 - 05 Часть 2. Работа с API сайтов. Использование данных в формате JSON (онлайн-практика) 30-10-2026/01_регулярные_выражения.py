"""
re - маска, которую можно "надеть" на текст и проверить соответствует ли текст этой маске
"""

"""
Match   match = re.search(regex, string)
"""

import re

print('\n---re.match--------------------')
res = re.match(r'AV', 'AV_Avia')    # match - отрабатывает если в начале строки есть совпадение
print(res)  # <re.Match object; span=(0, 2), match='AV'>
res = re.match(r'AV', 'A1V_Avia')
print(res)  # None

print('\n---re.search--------------------')

res = re.search(r'AV', '1AV_Avia')  # search - ищет во всей строке и выдает первое совпадение
print(res)  # <re.Match object; span=(1, 3), match='AV'>
res = re.search(r'.V', 'regAV_AviaAV/AV')  # search - ищет во всей строке
print(res)  # <re.Match object; span=(3, 5), match='AV'>

print('\n---re.findall--------------------')

res = re.findall(r'AV', 'regAV_AviaAV/AV')  # выдает список всех совпадений
print(res)  # ['AV', 'AV', 'AV']

print('\n---re.finditer--------------------')
res = re.finditer(r'AV', 'regAV_AviaAV/AV')  # выдает итератор
print(next(res))    # <re.Match object; span=(3, 5), match='AV'>
print(next(res))    # <re.Match object; span=(10, 12), match='AV'>
print(next(res))    # <re.Match object; span=(13, 15), match='AV'>

print('\n---re.fullmatch--------------------')
res = re.fullmatch(r'AV', 'regAV_AviaAV/AV')  # полное совпадение строки
print(res)    # None
res = re.fullmatch(r'regAV_AviaAV/AV', 'regAV_AviaAV/AV')  # полное совпадение строки
print(res)    # <re.Match object; span=(0, 15), match='regAV_AviaAV/AV'>


print('\n---re.sub--------------------')
res = re.sub(r'что меняем', 'на что меняем', 'где меняем')  #

print('\n---re.split--------------------')
res = re.split(r'p', 'perspective')  #
print(res)  # ['', 'ers', 'ective']
res = re.split(r'p', 'perspective', maxsplit=1)  #
print(res)  # ['', 'erspective']
res = re.split(r'p', 'PerspectivPe', maxsplit=1, flags=re.IGNORECASE)  #
print(res)  # ['', 'erspectivPe']

print('\n---re.sub--------------------')
pattern = re.compile(r'AV')  #
res = pattern.findall('regAV_AviaAV/AV')
print(res)  # ['AV', 'AV', 'AV']

# """
# СПЕЦСИМВОЛЫ
# \d - любая цифра
# \D - любое не числовое значение
#
# \s - символы пробелов
# \S - все, кроме символов пробелов
#
# \w - буква, цифра и нижнее подчеркивание
# \W - все, кроме буквы, цифры и нижнего подчеркивания
#
# . - любой символ кроме переноса строки
# ^ - начало строки   # ^...
# $ - конец строки    # ...$
# [abc] - любой символ в скобках
# [^abc] - любой символ кроме тех что в скобках
# a|b - a или b
# (ab) - определяем одним элементом
# \bслово\b
# """


print('\n---^[^abc]--------------------')
result = re.findall(r'^[abc]', 'aligol6573@gmail.com')
print(result)   # ['a']
result = re.findall(r'[^abc]', 'aligol6573@gmail.com')
print(result)   # ['l', 'i', 'g', 'o', 'l', '6', '5', '7', '3', '@', 'g', 'm', 'i', 'l', '.', 'o', 'm']
result = re.findall(r'[abc]', 'aligol6573@gmail.com')
print(result)   # ['a', 'a', 'c']

print('\n---(ab)--------------------')
result = re.findall(r'(al)i', 'aligol6573@gmail.com')
print(result)   # ['a']


"""КВАНТИФИКАТОРЫ
regex+ - встречается один или более раз
regex* - встречается ноль или более раз
regex? - встречается ноль или один раз
regex{n} - встречается n раз
regex{n, m} - встречается от n до m раз

"""

print('\n---regex--------------------')
regex = re.compile(r'^.+#') # все символы с начала строки до решетки
print(regex.findall('d_r56#'))  # ['d_r56#']

regex = re.compile(r'^.+#') # все символы с начала строки до решетки
print(regex.findall('d_r56#dghmgfjhfhj,'))  # ['d_r56#'] то есть дальше # ничего не возьмется

regex = re.compile(r'\S+$') #
print(regex.findall('d_r56# '))  # []