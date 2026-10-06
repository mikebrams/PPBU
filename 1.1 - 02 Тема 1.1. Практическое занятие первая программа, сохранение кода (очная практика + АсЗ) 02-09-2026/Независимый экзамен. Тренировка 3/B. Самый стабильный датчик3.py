import time

start_time = time.time()

from operator import itemgetter

sensors, tests = map(int, input().split())

sensors_list =[]

for _ in range(1, sensors + 1):
    input_data = input().split()     # ввод датчика и измерений

    sensor_current = input_data[0]                   # срез - нахождение имени датчика
    results_nums = tuple(map(int, input_data[1:]))    # срез - выборка измерений и перевод его в list[int]

    spread = max(results_nums) - min(results_nums)      # разброс между макс и мин значениями датчиков
    average_data = sum(results_nums) / tests            # среднее значение показателей

    sensors_list.append(( int(spread), int(average_data),  sensor_current))

new_sensors_list = sorted(sensors_list, key=itemgetter(0, -1, 2))
# new_sensors_list = sorted(sensors_list, key=itemgetter(1), reverse=True)
# new_sensors_list = sorted(sensors_list, key=itemgetter(2))

for i in range(sensors):
    print(new_sensors_list[i][2])


end_time = time.time()
execution_time = end_time - start_time  # Вычисляем разницу

print(f"Время выполнения: {execution_time:.4f} секунд")


"""
4 5
alpha 10 12 11 10 12
beta 8 8 9 9 8
gamma 20 21 22 21 20
delta 5 6 5 6 5
"""

# [(2, 11, 'alpha'), (1, 8, 'beta'), (2, 20, 'gamma'), (1, 5, 'delta')]
# [(1, 8, 'beta'), (1, 5, 'delta'), (2, 11, 'alpha'), (2, 20, 'gamma')]
# [(2, 20, 'gamma'), (2, 11, 'alpha'), (1, 8, 'beta'), (1, 5, 'delta')]
# [(2, 11, 'alpha'), (1, 8, 'beta'), (1, 5, 'delta'), (2, 20, 'gamma')]
# [(2, 11, 'alpha'), (1, 8, 'beta'), (1, 5, 'delta'), (2, 20, 'gamma')]

"""
beta
delta
gamma
alpha
"""