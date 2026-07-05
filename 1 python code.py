import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Turtle Animation")

t = turtle.Turtle()
t.speed(0)          
t.width(2)
t.hideturtle()

h = 0

for i in range(360):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)

    t.circle(i * 0.4)
    t.left(10)

    h += 0.005

    screen.update()

turtle.done()