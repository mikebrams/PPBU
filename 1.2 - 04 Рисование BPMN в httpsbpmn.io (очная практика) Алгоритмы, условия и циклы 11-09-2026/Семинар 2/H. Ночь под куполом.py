h = int(input())    # h целых часов, 1–24
d = int(input())    # выходной ли день (0 — будний, 1 — выходной)
s = int(input())    # есть ли членство в клубе (0 или 1)


value = 0

if d:
    if h <= 2:
        value = h * 100
    else:
        value += h * 80
else:
    if h <= 2:
        value += h * 80
    elif h <= 5:
        value += h * 60
    else:
        value += h * 40

if s:
    print(int(value * 0.75))
else:
    print(value)