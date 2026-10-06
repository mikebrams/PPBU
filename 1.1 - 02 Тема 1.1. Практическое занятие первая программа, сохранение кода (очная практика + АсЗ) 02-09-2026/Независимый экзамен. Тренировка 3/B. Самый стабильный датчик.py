# sensors, tests = map(int, input().split())
#
# min_spread = 2_000
#
# sensors_list =[]
#
# average_data = 2_000
#
# dict_sensors = {}
#
# for i in range(1, sensors + 1):
#     results = input().split()
#     tests = list(map(int, results[1:]))
#
#     dict_sensors[results[0]] = tests
#
# print(dict_sensors)


#     results_nums = list(map(int, results[1:]))
#
#
#     spread = max(results_nums) - min(results_nums)
#
#
#     if spread <= min_spread:
#         min_spread = spread
#         sensors_list.insert(0, results[0])
#
# print(sensors_list)

import operator

action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": operator.pow
}

print(action['-'](50, 25))
# 25
action['+'](50, 25)
# 75
action['/'](50, 25)
# 2.0
action['*'](50, 25)
# 1250

print('-' * 50) # -------------------------------------------------------------------------------

# Сортировка словаря на основе функции len
l1 = {'carrot': 'vegetable', 'red': 'color', 'apple': 'fruit'}

# Возвращает список ключей, отсортированных по функции len
print(sorted(l1, key=len))

# Возвращает список значений, отсортированных на основе функции len
print(sorted(l1.values(), key=len))

print('-' * 50) # -------------------------------------------------------------------------------

d1 = {'apple': 1, 'Banana': 2, 'Pears': 3}
# Возвращает список ключей, отсортированный по значениям
print(sorted(d1))
# Вывод: ['Banana', 'Pears', 'apple']

# Возвращает список ключей, отсортированный после применения str.lower ко всем элементам
print(sorted(d1, key=str.lower))
# Вывод: ['apple', 'Banana', 'Pears']

print('-' * 50) # -------------------------------------------------------------------------------

# напишем функцию для получения второго элемента
def sort_key(e):
    return e[1]

l1 = [(1, 2, 3), (2, 1, 3), (11, 4, 2), (9, 1, 3)]
# По умолчанию сортировка выполняется по первому элементу
print(sorted(l1))
# Вывод: [(1, 2, 3), (2, 1, 3), (9, 1, 3), (11, 4, 2)]

# Сортировка по второму элементу с помощью функции sort_key
print(sorted(l1, key=sort_key, reverse=True))
# Вывод: [(2, 1, 3), (9, 1, 3), (1, 2, 3), (11, 4, 2)]

print('-' * 50) # -------------------------------------------------------------------------------

class Student:
    def __init__(self, name, rollno, grade):
        self.name = name
        self.rollno = rollno
        self.grade = grade

    def __repr__(self):
        return f"{self.name}-{self.rollno}-{self.grade}"

# Создание объектов
s1 = Student("Paul", 15, "second")
s2 = Student("Alex", 12, "fifth")
s3 = Student("Eva", 21, "first")
s4 = [s1, s2, s3]

# Сортировка списка объектов
# Создание lambda-функции, которая вернет rollno объекта
s5 = sorted(s4, key=lambda x: x.rollno)
print(s5)
# Вывод: [Alex-12-fifth, Paul-15-second, Eva-21-first]

