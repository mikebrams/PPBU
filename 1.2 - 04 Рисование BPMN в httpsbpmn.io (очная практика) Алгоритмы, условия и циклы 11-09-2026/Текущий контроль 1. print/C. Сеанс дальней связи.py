h = int(input()) * 3600
m = int(input())

value = 0

if m <= 5:
    value += m * 20
elif m <= 20:
    value = 5 * 20 + (m - 5) * 12
else:
    value = 5 * 20 + 15 * 12 + (m - 20) * 8

if h >= 79200 or h <= 21540:
    print(int(value * 0.75))
else:
    print(value)