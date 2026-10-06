n = int(input())

users = list(map(int, input().split()))

min_index = min(users)

print(users.index(min_index))