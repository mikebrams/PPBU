n = int(input())    # количество грузовых модулей
k = int(input())    # вместимость одной капсулы
b = int(input())    # стоимость запуска одной капсулы
p = int(input())    # стоимость погрузки одного модуля


quan_k = n // k + (1 if n % k != 0 else 0)  # кол-во капсул
free_seat = 0 if n % k == 0 else k - n % k

energy = n * p + quan_k * b

print(quan_k, free_seat, energy, sep='\n')