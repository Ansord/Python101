
import turtle
tao = turtle.Pen()
tao.shape('turtle')
tao.pensize(10)

tao.circle(45)

tao.color("red")
tao.penup()

tao.penup()
tao.goto(110,0)
tao.pendown()
tao.circle(45)

tao.color("blue")
tao.penup()
tao.goto(-110,0)
tao.pendown()
tao.circle(45)

tao.color("yellow")
tao.penup()
tao.goto(-55,-45)
tao.pendown()
tao.circle(45)

tao.color("green")
tao.penup()
tao.goto(55,45)
tao.goto(55,-45)
tao.pendown()
tao.circle(45)
