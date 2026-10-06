n = int(input())

ns = list(map(int, input().split()))

print(n-1)
for i in range(1, n):
    print(ns[n - 1 - i], end=' ')