# Brandon R. Cruz
# 3 JULY 2025
# P4LAB1- SHAPES
# Prgram that enables the user to draw two shapes.


import turtle

t = turtle.Turtle()
t.pensize(3)
t.speed(2)


for side in range(4):
    t.forward(100)
    t.right(90)


t.penup()
t.goto(150, 0)
t.pendown()


for side in range(3):
    t.forward(100)
    t.left(120)


turtle.done()

