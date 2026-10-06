def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль"
    except TypeError:
        return "Ошибка типа данных"

def log(result):
    with open("calculations.txt", "a", encoding='utf-8') as f1:
        f1.write(str(result) + "\n")  # добавлен перевод строки для читаемости

def check_int(prompt: str):
    while True:
        value = input(prompt)
        if value.lstrip('-').isdigit():
            return int(value)
        else:
            print('Это не целое число. Нужно ввести целое число.\n')

print("Выберите операцию: ")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Просмотр истории вычислений")

choice = input("Введите номер операции (1/2/3/4/5): ")

valid_choices = ['1', '2', '3', '4', '5']

while choice not in valid_choices:
    choice = input("\nНеверный ввод. Пожалуйста, выберите 1, 2, 3, 4 или 5: ")

if choice == '5':
    try:
        with open("calculations.txt", "r", encoding='utf-8') as f2:
            history = f2.read()
        print(f'История вычислений:\n{history}')
    except FileNotFoundError:
        with open("calculations.txt", "a+") as f0:
            history = f0.read()
        print(f'История вычислений:\n{history}')

else:
    num1 = check_int("Введите первое число: ")
    num2 = check_int("Введите второе число: ")

    if choice == '1':
        r = f"Результат: {num1} + {num2} = {add(num1, num2)}"
        print(r)
        log(r)
    elif choice == '2':
        r = f"Результат: {num1} - {num2} = {subtract(num1, num2)}"
        print(r)
        log(r)
    elif choice == '3':
        r = f"Результат: {num1} * {num2} = {multiply(num1, num2)}"
        print(r)
        log(r)
    elif choice == '4':
        result = divide(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            result = f"Результат: {num1} / {num2} = {result:.2f}"
            print(result)
            log(result)
