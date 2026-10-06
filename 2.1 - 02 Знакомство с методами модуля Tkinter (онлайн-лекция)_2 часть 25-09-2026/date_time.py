from datetime import datetime, date, time, timedelta
from idlelib.replace import replace

d = date(2024, 12, 31)      # определение даты вручную
t = time(12, 31, 16)        # определение времени вручную
print(d, type(d))
print(t, type(t))

dt = datetime.combine(d, t)     # метод комбинирования даты и времени
print(dt, type(dt))


d = date.today()        # получение текущей даты
print(d)

d = datetime.now()      # получение текущей даты и времени  2026-09-25 16:31:52.222913
print(d.time())         #

d = datetime.now().replace(microsecond=0)      # получение текущей даты и времени   2026-09-25 16:31:52
print(d)


dt  = datetime.now()
dt = dt.replace(year=2000)
print(dt)

#-------------------------------------------------------------------------------------------------------

# Ввод даты из строки

# dtt = input('Введите дату (дд.мм.гггг): ')
#
# data = datetime.strptime(dtt, '%d.%m.%Y')
#
# print(data)
#
# print(data.strftime('%d.%m.%Y %X'))

#-------------------------------------------------------------------------------------------------------

# Развернутый вывод даты в кортеже

dt = datetime.now().replace(microsecond=0)
dtt = dt.timetuple()

print(dtt)  # time.struct_time(tm_year=2026, tm_mon=9, tm_mday=25, tm_hour=16, tm_min=57, tm_sec=34, tm_wday=4, tm_yday=268, tm_isdst=-1)

for i in dtt:
    print(i)

#-------------------------------------------------------------------------------------------------------

dtt = dt.isocalendar()
print(dtt)
print(dt.weekday())
print(dt.isoweekday())

days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

print(days[dt.weekday()])

#-------------------------------------------------------------------------------------------------------

# Расчет кол-ва дней до даты рождения

birthday = input('Введите дату рождения ("дд.мм.гггг"):')
birthday = datetime.strptime(birthday, '%d.%m.%Y').date()
today = date.today()

year = today.year

birthday = birthday.replace(year=year)

if birthday < today:
    birthday = birthday.replace(year=year + 1)
res = birthday - today

print(res)