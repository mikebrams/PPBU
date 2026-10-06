o = int(input())    # сведения о препятствии (0, 1 или 2)
b = int(input())    # целый заряд b (0–100)
g = int(input())    # (0 — твёрдый, 1 — мягкий)


if o == 2:
    print('STOP')
elif o == 1:
    if g == 0 and b >= 40:
        print('DETOUR')
    else:
        print('WAIT')
else:
    if g == 1:
        if b >= 30:
            print('SLOW')
        else:
            print('CHARGE')
    else:
        if b >= 10:
            print('GO')
        else:
            print('CHARGE')