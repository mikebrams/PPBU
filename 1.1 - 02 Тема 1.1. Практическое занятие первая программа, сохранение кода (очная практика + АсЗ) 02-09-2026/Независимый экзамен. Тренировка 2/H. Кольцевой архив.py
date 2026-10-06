n       = int(input())
frames  = list(map(int, input().split()))
k       = int(input())          # Если k > 0, последовательность сдвигается вправо, k < 0 - влево

diff = abs(n - abs(k))
shift = max(n, diff) % min(n, diff) if min(n, diff) else 0

new_frames = []

if not n or not k or not shift:
    new_frames = frames
elif k > 0:
    new_frames = frames[-shift:] + frames[:n - shift]
else:
    new_frames = frames[shift:] + frames[:shift]

print(*new_frames, sep=' ')



# print(shift)

"""
5
10 20 30 40 50
22

5
10 20 30 40 50
-22

0
1 2 3 4
0

4
1 2 3 4
4

1
0
1



"""
# print(5 % -50)
# print(5 % -49)
# print(5 % -44)
# print(5 % 50)
# print(5 % 49)
# print(5 % 44)


#
# new_frames = []
#
# if not k_pos or not shift or not n_frames:
#     print(*frames, sep=' ')
# elif k_pos > 0:
#     board = n_frames - shift
#     new_frames = frames[board:] + frames[:board]
# else:
#     new_frames = frames[shift:] + frames[:shift]
#
# print(*new_frames, sep=' ')


# print(shift)

# if not shift:
#     print(frames)



# if n_frames % 2:
# shift_left  = abs(n_frames - k_pos)
# shift_right = abs(n_frames - k_pos)


# 7 - 2 = 5
# 7 + 2 = 2
# 7 - 5 = 2
# 7 + 5 = 5

# 7 - 1 = 6         7 - 1
# 7 + 1 = 1
# 7 - 3 = 4
# 7 + 3 = 3


# 10 20 30 40 50 60 70 | 10 20 30 40 50 60 70 | 10 20 30 40 50 60 70 | 10 20 30 40 50 60 70



# print(7 % 1)
# print(100 % 50)