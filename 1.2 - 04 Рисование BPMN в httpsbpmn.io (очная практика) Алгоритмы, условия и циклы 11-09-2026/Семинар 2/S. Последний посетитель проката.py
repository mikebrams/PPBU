
Flag = True
good = 0
bad = 0

while Flag:
    n = int(input())
    if n == 1:
        good += 1
    elif n == 2:
        bad += 1
    if n == 0:
        Flag = False

print(f'{good} {bad}')