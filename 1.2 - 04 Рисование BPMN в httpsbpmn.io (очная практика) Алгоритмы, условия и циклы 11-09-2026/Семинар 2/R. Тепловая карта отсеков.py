r, c, t = map(int, input().split())

# r - ряд               1 <= r
# c - по 'c' датчиков   с <= 30
# t - температура       -50 <= t <= 100         t


max_t = -60
num_r = 0
num_c = 0


for i in range(r):
    danger_sensor = 0
    sensors = list(map(int, input().split()))
    for s in range(c):
        if sensors[s] >= t:
            danger_sensor += 1

        if sensors[s] > max_t:
            max_t = sensors[s]
            num_r = i + 1
            num_c = s + 1

    print(danger_sensor)

print(max_t, num_r, num_c)