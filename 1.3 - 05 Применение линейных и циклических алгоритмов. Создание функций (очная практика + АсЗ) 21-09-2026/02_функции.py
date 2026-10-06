# def get_number(prompt):
#     while True:
#         value = input(prompt)
#         if value.isdigit():
#             return int(value)
#         else:
#             print("Это не целое число. Пожалуйста, введите целое число.")
#
# num1 = get_number("Введите первое число: ")
# num2 = get_number("Введите второе число: ")


def get_number(prompt):
    while True:
        value = input(prompt)
        if value.lstrip('-').isdigit():
            if int(value) >= 0:
                return int(value)
            else:
                print("Это отрицательное число. Пожалуйста, введите целое положительное число.")
        else:
            print("Это не целое число. Пожалуйста, введите целое положительное число.")

num1 = get_number("Введите первое число: ")
num2 = get_number("Введите второе число: ")

a = '1'

