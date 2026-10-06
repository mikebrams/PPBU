n = int(input())

value = 0

for i in range(n):
    price, count = map(int, input().split())
    value += price * count

print(value)

