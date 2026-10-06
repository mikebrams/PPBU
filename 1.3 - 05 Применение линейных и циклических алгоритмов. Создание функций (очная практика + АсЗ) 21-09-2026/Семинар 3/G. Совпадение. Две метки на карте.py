x1, y1, x2, y2 = map(int, input().split())

point = x1 == x2 and y1 == y2

print('YES' if point else 'NO')