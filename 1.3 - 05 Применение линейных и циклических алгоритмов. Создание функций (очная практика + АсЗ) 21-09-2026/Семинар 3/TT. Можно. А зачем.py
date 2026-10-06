ax, ay, bx, by, cx, cy = list(map(int, input().split()))

strait = abs(ax - bx) + abs(ay - by)
AC = abs(ax - cx) + abs(ay - cy)
BC = abs(cx - bx) + abs(cy - by)

print(AC + BC - strait)