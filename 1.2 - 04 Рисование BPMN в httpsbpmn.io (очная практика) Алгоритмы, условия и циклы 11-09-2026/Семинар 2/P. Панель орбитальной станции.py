r, c = map(int, input().split())    # ряд, столбец

for i in range(1, r+1):
    for j in range(1, c+1):

        if i == 1 or i == r:
            print("#", end="")
        elif j == 1 or j == c:
            print("#", end="")
        elif i == j:
            print("*", end="")
        elif (i + j) % 2 == 0:
            print(".", end="")
        else:
            print(":", end="")
    print()