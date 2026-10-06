def shift_point(point, dx, dy):
    return point[0]+dx, point[1]+dy


print(shift_point((2, 3), -1, 4))
print(shift_point((0, 0), 0, 0))
print(shift_point((-1000, 1000), 1000, -1000))
print(shift_point((1, 1), -2, -3))
print(shift_point(point=(0, 1), dx=2, dy=3))