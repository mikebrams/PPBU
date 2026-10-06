a, b, q = map(int, input().split())

if a + b < q:
    print('NO_DATA')
elif b * 2 <= a:
    print('BASE')
elif a * 2 <= b:
    print('CRINGE')
else:
    print('MIXED')