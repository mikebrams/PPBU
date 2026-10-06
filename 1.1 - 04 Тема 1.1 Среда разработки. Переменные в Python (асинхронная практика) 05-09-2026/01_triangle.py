import turtle as t

t.colormode(255)
t.speed(20)
t.pensize(3)
t.color('blue')
# t.rt(60)
for i in range(4, 56, 4):
    t.color('blue')
    t.begin_fill()
    t.fillcolor(2, 2, 2)
    t.circle(i)
    t.fd(i)
    t.rt(90)
    t.end_fill()

# t.rt(270)
# for j in range(52, 0, -4):
#     t.color('red')
#     # t.circle(j)
#     t.fd(j)
#     t.rt(90)
#
t.mainloop()