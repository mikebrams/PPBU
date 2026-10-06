import turtle as t

# t.colormode(255)
#
# t.ht()
#
# t.pensize(5)
#
# for r in range(160, 0, -40):
#     for i in range(6):
#         t.color(255, 165, int(r/4) * 6)
#
#         t.fillcolor(162, int(r/4) * 6, 255)
#
#         t.begin_fill()
#
#         for _ in range(4):
#             t.forward(r)
#             t.right(90)
#
#         # t.circle(r)
#
#         t.end_fill()
#
#         t.rt(60)




for i in range(3):

    t.begin_fill()

    for _ in range(4):
        t.forward(30)
        t.left(90)

    t.penup()
    t.forward(60)
    t.pendown()

t.mainloop()
