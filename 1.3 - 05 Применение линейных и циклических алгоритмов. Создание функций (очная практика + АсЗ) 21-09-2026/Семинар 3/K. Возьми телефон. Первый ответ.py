n = int(input())
calls = list(map(int, input().split()))

if 1 in calls:
    print(calls.index(1))
else:
    print(-1)



