import matplotlib.pyplot as plt

def add(v1, v2):
    x = v1[0] + v2[0]
    y = v1[1] + v2[0]
    return x, y


v1 = (10, 5)  # вектор - его позиции 10 и 5, выходят из 0 и 0
v2 = (3, 15)
v = v1 + v2  # (10, 5, 3, 15) - что неправильно
print(v)
v = add(v1, v2)
print(v)  # (13, 8) - правильно



class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    # def display_add(self, other):
    #     res = self + other
    #     x1 = [0, self.x]
    #     y1 = [0, self.y]
    #     x2 = [0, other.x]
    #     y2 = [0, other.y]
    #     rx = [0, res.x]
    #     ry = [0, res.y]
    #
    #     plt.plot(x1, y1, x2, y2, rx, ry, '-.g')
    #     plt.show()


    def __str__(self):
        return f'V({self.x}, {self.y})'

v1 = Vector(10, 5)
v2 = Vector(3, 15)
v3 = Vector(2, 4)

print(v1)
print(v1 + v2)


# v1.display_add(v2)

""" S O L I D """


# class Person:
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#     def __str__(self):
#         return f'{self.name} is {self.age} years old'
#
#
# ps1 = Person('Mary', 18)
# ps2 = Person('Pit', 19)
# ps3 = Person('Dasha', 19)
#
# print(ps1)
# print(ps1.name)
#
# ps1.name = 'Sasha'
# print(ps1.name)
