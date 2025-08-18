import turtle
import math


def drawTriangle(t: turtle.Turtle, pos: tuple[int, int], size: int) -> None:
    t.penup()
    t.goto(pos)
    t.setheading(90)
    t.pendown()
    for _ in range(3):
        t.forward(size)
        t.left(120)


def drawSquare(t: turtle.Turtle, pos: tuple[int, int], size: int) -> None:
    t.penup()
    t.goto(pos)
    t.setheading(90)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.right(90)


def drawCircle(t: turtle.Turtle, pos: tuple[int, int], radius: int) -> None:
    t.penup()
    t.goto(pos[0], pos[1] - radius)
    t.setheading(90)
    t.pendown()
    t.circle(radius)


def drawPolygon(t: turtle.Turtle, pos: tuple[int, int], size: int, sides: int) -> None:
    t.penup()
    t.goto(pos)
    t.setheading(90)
    t.pendown()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)


def drawHouse(t: turtle.Turtle, pos: tuple[int, int], size: int) -> None:
    diagLength = math.sqrt(size ** 2 * 2)
    t.setheading(90)
    t.penup()
    t.goto(pos)
    t.pendown()
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(135)
    t.forward(diagLength)
    t.right(135)
    t.forward(size)
    t.right(135)
    t.forward(diagLength)
    t.left(90)
    t.forward(diagLength // 2)
    t.left(90)
    t.forward(diagLength // 2)
    t.left(45)
    t.forward(size)


t = turtle.Turtle()
t.speed(1)
drawTriangle(t, (0, 0), 50)
drawSquare(t, (100, 0), 50)
drawCircle(t, (200, 0), 50)
drawPolygon(t, (300, 0), 50, 6)
drawHouse(t, (-200, 0), 50)
turtle.done()