b = int(input())    # заряд аккумулятора в процентах;
w = int(input())    # скорость бокового ветра в м/с;
v = int(input())    # видимость в метрах;
d = int(input())    # расстояние до станции в метрах.


if b < 10 or b < 20 and d > 500:
    print('EMERGENCY')
elif w > 25 or v < 100:
    print('CLOSED')
elif b >= 30 and w <= 12 and v >= 800:
    print('AUTO')
elif b >= 20 and w <= 20 and v >= 300:
    print('MANUAL')
else:
    print('WAIT ')