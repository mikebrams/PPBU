n, l, r = map(int, input().split())

meteors = 0
weight = 0

for i in range(n):
    w = int(input())
    if l <= w <= r:
        meteors += 1
        weight += w

print(meteors, weight)