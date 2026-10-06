num = int(input())

for _ in range(9876 - num):
    num += 1
    # print(num)
    if len(set(str(num))) == 4:
        print(num)
        break



