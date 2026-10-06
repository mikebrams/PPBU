"""
Этапы работы программы

1. Ввод данных
2. Обработка данных
3. Вывод информации
"""


x = 7
y = 5.45
name = 'Mary'
yes_no = True

print(x - yes_no)

print(type(name))
print(type(x))

print()

print(x, y, '\n', name)

print(x, y, '\n' + name)    # делаем конкатенацию, чтобы убрать в начале строки пробел



x = 7  # int
y = 5.45  # float
name = 'Mary'  # str
yes_no = True  # bool yesNo
##x = '8'
##print(type(name + str(y)))
##print(type(x))
##print(name)
##print(yes_no)
##print(name + str(y)) # конкатенация
print (x, y, name, sep='\n') # \n = сепаратор: перенос по сторкам
##print (x, y, name, sep='...', end = '\n')
print (x, y, name, sep='...', end = '\\/')
print (x, y, name)
print (x, y, '\n', 12, yes_no)


a = 5 # 101 в двоичной системе
b = 3 # 011 в двоичной системе
print(a ^ b) # Вывод: 6 (110 в двоичной системе)


print("Он сказал, \"Привет, Мир!\"")


total = (1 + 2 + 3 +
4 + 5 + 6)
print(total) # Вывод: 21

print("Пример\rВозврат каретки")

print(__doc__) # Печать комментариев в файле (модуле)

print(False and False or True or False)

