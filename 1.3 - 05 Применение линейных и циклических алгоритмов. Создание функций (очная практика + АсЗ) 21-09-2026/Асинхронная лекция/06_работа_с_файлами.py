try:
    with open('proba2.txt', 'w', encoding='utf-8') as file:
        file.write('Пробный текст')
except IOError:
    print('Ошибка ввода-вывода')
except OSError:
    print('Ошибка операционной системы')
except UnicodeEncodeError:
    print('Ошибка кодирования текста')
except Exception as e:
    print(f'Неизвестная ошибка: {e}')

