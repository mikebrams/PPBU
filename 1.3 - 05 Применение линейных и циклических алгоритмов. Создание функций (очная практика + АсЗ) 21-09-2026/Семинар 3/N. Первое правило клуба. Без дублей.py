n = int(input())

count = 0
names = []

for i in range(n):
    name = input()
    if name in names:
        continue
    else:
        names.append(name)
        count += 1

print(count)
print(*names)