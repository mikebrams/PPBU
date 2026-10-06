try:
    n = int(input('> '))
    if n == 100:
        raise TypeError('Число 100 запрещено к использованию')  # самостоятельно делаем ограничения
    print(n)
except (ValueError, ZeroDivisionError):
    print('Введите число')
except NameError:
    print('Введите имя')
except Exception as err:        # все ошибки разом
    print(err)
else:
    print('Когда нет ошибки')
finally:
    print('Выполняется всегда')

