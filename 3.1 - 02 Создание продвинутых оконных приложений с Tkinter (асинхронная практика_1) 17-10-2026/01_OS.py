import os
from datetime import datetime

# os.mkdir('work')
file = 'work.txt'
dir_ = 'D:\\Projects\\OsnovaniePy2026\\3.1 - 02 Создание продвинутых оконных приложений с Tkinter (асинхронная практика_1) 17-10-2026'
filepath = os.path.join(dir_, file)

print(filepath)

last_time = os.path.getmtime('3.1.3+Листинги (1).docx')
a = datetime.fromtimestamp(last_time).strftime("%Y-%m-%d %H:%M:%S")
print(a)

b = os.path.exists('work')
print(b)
