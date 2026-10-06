a, b, s, k = map(int, input().split())


# a - батарея   1 <= a
# b - батарея        b <= 20
# s - единицы энергии   0 <= s <= 300
# k - кол-во батарей    0 <= k <= 30

counter = 0

for i in range(k+1):
    for j in range(k+1):
        if (i * a + j * b == s) and (i + j <= k):
            counter += 1
            print(f'{i} {j}')

if not counter:
    print('NONE')
