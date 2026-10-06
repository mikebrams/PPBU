n = int(input())

datas = []

for i in range(n):
    a, b = map(int, input().split())
    datas.append((a, b))

print(datas)


index_39 = datas.index((3, 9))

new_datas = datas[index_39:] + datas[:index_39]

print(index_39)

for i in new_datas:
    print(f'{i[0]} {i[1]}')
