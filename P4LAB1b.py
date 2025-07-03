import turtle

t = turtle.Turtle()

t.pensize(5)
t.color("blue")
t.speed(1)

# Draw B
for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.left(90)
t.forward(100)
t.pendown()

for i in range(3):
    t.forward(100)
    t.right(90)

# Move to the starting position for C
t.penup()
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(180)
t.pendown()

# Draw C
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)
