def lights(n):
    if n % 3 + n % 5 == 0:
        return 'BOTH'
    elif n % 3 == 0:
        return 'BLUE'
    elif n % 5 == 0:
        return 'RED'
    else:
        return 'WHITE'

for i in range(1, int(input())+1):
    print(f'{i} {lights(i)}')
