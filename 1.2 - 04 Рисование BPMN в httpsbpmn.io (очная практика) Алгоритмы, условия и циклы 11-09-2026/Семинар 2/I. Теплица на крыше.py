t = int(input())    # целая температура t (от −50 до 60)
h = int(input())    # влажность h (от 0 до 100)
s = int(input())    # признак дыма s (0 — нет, 1 — есть)


if s:
    print('ALARM')

else:
    if t < 10:
        print('HEAT')
    elif t > 30:
        if h < 40:
            print('MIST')
        else:
            print('COOL')
    else:
        if h < 30:
            print('WATER')
        elif h > 80:
            print('VENT')
        else:
            print('HOLD')




