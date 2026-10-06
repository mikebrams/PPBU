# for _ in 23, 45, 22, 32:
#     print('YES')

# YES
# YES
# YES
# YES

# for i in 23, 45, 22, 32:
#     print(i, 'YES')

# 23 YES
# 45 YES
# 22 YES
# 32 YES

for i in range(0, 10, 2):
    print(i, end=' ')
print()
print(i)


for i in range(1, 9):
    for j in range(1, 9):
        print(f'{i * j:>2}', end=' ')
    print()