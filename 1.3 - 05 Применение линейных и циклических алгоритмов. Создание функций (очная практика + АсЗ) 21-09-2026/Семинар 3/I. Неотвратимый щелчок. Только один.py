n = int(input())
av = list(map(int, input().split()))

print(*av[::2])