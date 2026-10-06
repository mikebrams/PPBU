n = int(input())

for i in range(n):
    r, e = map(int,input().split())
    print(r*2 - e, end=' ')