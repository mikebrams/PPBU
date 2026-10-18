num = input()
chars = '0123456789'

if len(num) != 5 or num[2] != ':':
    print('Формат неверный')
else:
    for i in [0, 1, 3, 4]:
        if num[i] not in chars:
            print('Формат неверный')
            break
    else:
        print('Формат верный')

