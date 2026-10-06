n       = int(input())
frames  = list(map(int, input().split()))
k       = int(input())

if not k or not n:
    print(*frames, sep=' ')
else:
    shift = k % n
    frames = frames[-shift:] + frames[:-shift]
    print(*frames, sep=' ')


"""
print(2 % 10)       2   
print(-2 % 10)      8

10
10 20 30 40 50 60 70 80 90 100
-2

30 40 50 60 70 80 90 100 10 20



10
10 20 30 40 50 60 70 80 90 100
2

90 100 10 20 30 40 50 60 70 80


-5 % 5 = 0
-4 % 5 = 1
-3 % 5 = 2
            -2 % 5 = 3   #
-1 % 5 = 4
1 % 5 = 1
             2 % 5 = 2   #
3 % 5 = 3
4 % 5 = 4
5 % 5 = 0

                -22 % 5 = 3
                 22 % 5 = 2

"""


# print(2 % 10)
# print(-2 % 10)



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
