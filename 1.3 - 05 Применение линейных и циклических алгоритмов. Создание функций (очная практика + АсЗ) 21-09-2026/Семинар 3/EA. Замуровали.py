h, w = map(int, input().split())

count = 0
matrix = []
free_cell = []

for i in range(h):
    sign = input()
    for j in range(w):
        if sign[j] == '.':
            free_cell.append((i, j))


pos = tuple(map(int, input().split()))


matrix.append((pos[0] - 1, pos[1]))
matrix.append((pos[0], pos[1] - 1))
matrix.append((pos[0] + 1, pos[1]))
matrix.append((pos[0], pos[1] + 1))

for i in matrix:
    if i in free_cell:
        count += 1

print(count)