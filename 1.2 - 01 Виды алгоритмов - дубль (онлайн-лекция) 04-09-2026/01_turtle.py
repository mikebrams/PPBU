from turtle import *

colormode(255)
pensize(4)
speed(25)
r = 255
g = 255
b = 0

br = 0
bg = 255
bb = 0

shape('classic')
# hideturtle()

color((br, bg, bb), (r, g, b))          # цвет линии, цвет заполнения

for j in range(150, 10, -25):
    # fillcolor(r, g, b)
    color((br, bg, bb), (r, g, b))
    for i in range(8):
        # fillcolor(r, g, b)
        begin_fill()
        circle(j)
        end_fill()
        rt(45)      # поворот черепахи на заданное кол-во градусов

    r -= 30
    g -= 15
    b += 30

    br += 30
    bg -= 30
    bb += 30

mainloop()      # оставляет открытым окно