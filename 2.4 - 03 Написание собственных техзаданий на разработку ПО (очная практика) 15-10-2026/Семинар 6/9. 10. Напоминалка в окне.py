from tkinter import *
from tkinter import messagebox as mb

def is_time(s):
    print(s)
    if len(s) != 5:
        return False
    elif not (s[0]+s[1]+s[3]+s[4]).isdigit() or s[2] != ':':
        return False
    elif int(s[0]+s[1]) not in range(24) or int(s[3]+s[4]) not in range(60):
        return False
    else:
        return True


def set_alarm():

    now = e1.get()
    alarm = e2.get()
    check_time = is_time(now)
    check_alarm = is_time(alarm)

    if not check_time or not check_alarm:
        mb.showerror('Ошибка', 'Время нужно в формате ЧЧ:ММ')
        result.config(text='Напоминание не поставлено')
    else:
        n_h, n_m = int(now[0:2]), int(now[3:])
        a_h, a_m = int(alarm[0:2]), int(alarm[3:])

        now_ = n_h * 60 + n_m
        alarm_ = a_h * 60 + a_m

        if now_ == alarm_:
            result.config(text='Сработает через 0 ч 0 мин')
        elif alarm_ > now_:
            res = alarm_ - now_
            result.config(text=f'Сработает через {res // 60} ч {res % 60} мин')
        else:
            res = 1440 - now_ + alarm_
            result.config(text=f'Сработает через {res // 60} ч {res % 60} мин')


root = Tk()
root.title('Напоминалка')
root.geometry('250x110')

l1 = Label(root, text='Сейчас:')
l1.grid(column=0, row=0)

e1 = Entry(root)
e1.grid(column=1, row=0)

l2 = Label(root, text='Напомнить в:')
l2.grid(column=0, row=1)

e2 = Entry(root)
e2.grid(column=1, row=1)


b = Button(root, text='Поставить', command=set_alarm)
b.grid(column=1, row=2)

result = Label(root, text='Напоминание не поставлено')
result.grid(column=1, row=3)

root.mainloop()


