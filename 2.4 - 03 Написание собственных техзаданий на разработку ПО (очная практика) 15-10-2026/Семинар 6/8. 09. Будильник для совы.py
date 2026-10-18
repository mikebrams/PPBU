now = input()
alarm = input()

n_h, n_m = int(now[0:2]), int(now[3:])
a_h, a_m = int(alarm[0:2]), int(alarm[3:])

now_ = n_h * 60 + n_m
alarm_ = a_h * 60 + a_m

if now_ == alarm_:
    print('Через 0 ч 0 мин')
elif alarm_ > now_:
    res = alarm_ - now_
    print(f'Через {res // 60} ч {res % 60} мин')
else:
    res = 1440 - now_ + alarm_
    print(f'Через {res // 60} ч {res % 60} мин')


