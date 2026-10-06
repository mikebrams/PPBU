n = int(input())

res = list(map(int, input().split()))

days_rez_zero = [i for i in res if i == 0]

print(len(days_rez_zero))