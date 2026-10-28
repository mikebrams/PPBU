""" S O L I D """


class Person:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Объект должен быть строкой')
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError('Объект должен быть числом')
        self.__age = new_age

    name = property(get_name, set_name)

    def __str__(self):
        return f'{self.name} is {self.age} years old'


ps1 = Person('Mary', 18)
ps2 = Person('Pit', 19)
ps3 = Person('Dasha', 19)

print(ps1.get_name())

ps1.set_name('Sasha')
print(ps1.name)

ps1.name = 'Mary'
print(ps1.name, ps1.age)
