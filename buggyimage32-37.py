#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)
ladybug.speed(10)
# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + (15*num_dots), ypos + (10*num_dots))
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  xpos = ypos + 30
  xpos = xpos + 10
  num_dots = num_dots + 1

# Legs
legsAngle = 0
ladybug.penup()
ladybug.goto(0,-35)
ladybug.setheading(-10)
ladybug.forward(40)
ladybug.pendown()
ladybug.pensize(5)
ladybug.forward(20)
for i in range(4):
  ladybug.penup()
  ladybug.goto(0,-35)
  ladybug.setheading(-20 + legsAngle)
  ladybug.forward(40)
  ladybug.pendown()
  ladybug.forward(40)
  legsAngle = legsAngle + 10
legsAngle = 0
for i in range(4):
  ladybug.penup()
  ladybug.goto(0,-35)
  ladybug.setheading(-200 + legsAngle)
  ladybug.forward(40)
  ladybug.pendown()
  ladybug.forward(40)
  legsAngle = legsAngle + 10


  



ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()