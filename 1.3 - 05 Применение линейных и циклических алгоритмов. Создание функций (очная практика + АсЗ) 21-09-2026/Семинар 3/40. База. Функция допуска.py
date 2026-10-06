def has_pass(points, threshold=10):
    return points >= threshold


print(has_pass(10))
print(has_pass(4, 7))
print(has_pass(0, 0))
print(has_pass(0, 1))
print(has_pass(1000, 1000))