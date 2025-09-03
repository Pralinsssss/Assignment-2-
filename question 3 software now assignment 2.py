import turtle

def draw_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        part = length / 3
        draw_edge(part, depth - 1)
        turtle.left(60)
        draw_edge(part, depth - 1)
        turtle.right(120)
        draw_edge(part, depth - 1)
        turtle.left(60)
        draw_edge(part, depth - 1)

def draw_shape(sides, length, depth):
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.right(360 / sides)

turtle.speed(0)
turtle.hideturtle()

sides = int(input("Enter number of sides: "))
length = int(input("Enter side length: "))
depth = int(input("Enter recursion depth: "))

draw_shape(sides, length, depth)
turtle.done()
