import math

from OOP4_абстрактный_класс import Shape


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Круг')
        self.radius = radius

    def calc_square(self):
        return math.pi * self.radius ** 2

    def display(self):
        super().display()
        print(f'Радиус: {self.radius} ед.\n'
              f'Площадь: {self.calc_square():.2f} кв.ед')

c = Circle(2)
c.display()
