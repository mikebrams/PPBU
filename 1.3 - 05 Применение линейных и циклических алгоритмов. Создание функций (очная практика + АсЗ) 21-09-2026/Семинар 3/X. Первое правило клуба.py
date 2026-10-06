string = list(input().split())

for i in range(len(string)):
    if string[i] == 'CLUB':
        string[i] = 'SECRET'

print(*string)