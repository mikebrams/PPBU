def greet(name="Гость"):
    print(f"Привет, {name}!")

result = greet('Михаил')

print(result)

def describe_pet(type, name):
    print(f"У меня есть {type} по имени {name}.")

describe_pet(type = 'хомяк', name = 'Гарри')
describe_pet(name = 'Гарри', type = 'хомяк')


def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Марат", greeting="Привет")


def func(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

func(1, 2, a = 3, b = 4)

print()

def example(*numbers, **details):
    print("Numbers:", numbers)
    print("Details:", details)

# Вызов функции
example(90, 60, 90, name = "Вика", age = 33)

print('-' * 95)

is_even = lambda x: x % 2 == 0
print(is_even(8))

print('-' * 95)

first_item = lambda l: l[0] if l else None
print(first_item("apple"))



