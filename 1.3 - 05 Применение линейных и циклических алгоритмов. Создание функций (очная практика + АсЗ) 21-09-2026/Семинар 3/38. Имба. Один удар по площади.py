"""
Способность бьёт по выбранной клетке и её восьми соседям.
В таблице записано здоровье целей; 0 — пустая клетка.
Цель уничтожается, если её здоровье положительно и не больше damage.
Посчитайте уничтоженные цели для уже выбранного места удара.
Искать лучшее место и считать суммарный урон не нужно.

3 3
0 3 0
8 0 2
0 0 7
1 1 3

1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1

3 3

2,2 2,3 2,4
3,2 3,3 3,4
4,2 4,3 4,4

"""

h, w = map(int, input().split())

matrix = [[0] * (w + 2) for i in range(h+2)]

for i in range(h):
    row = list(map(int, input().split()))
    for j in range(w):
        matrix[i+1][j+1] = row[j]

r, c, damage = map(int, input().split())

destroyed = 0

for i in range(3):
    for j in range(3):
        if 0 < matrix[r+i][c+j] <= damage:
            destroyed += 1

print(destroyed)
