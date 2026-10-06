h = int(input())
m = int(input())
s = int(input())
d = int(input())


t = h * 3600 + m * 60 + s
t = t + d

sec_sutki = 24 * 3600
sutki = t // sec_sutki

t = t % sec_sutki

h = t // 3600
t = t % 3600
m = t // 60
s = t % 60

print(sutki, h, m, s)