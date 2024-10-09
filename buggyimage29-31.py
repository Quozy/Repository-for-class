#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used

# Draw Body
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)

# Configure Spider Legs
l = 8
length = 90
angle = 360 / l
print(angle)
painter.pensize(5)
numLegDrawn = 0

# Draw Spider Legs
while (numLegDrawn < 4):
  painter.goto(0,0)
  painter.setheading((angle - 30) *numLegDrawn)
  painter.forward(length)
  numLegDrawn = numLegDrawn + 1
while (3 < numLegDrawn <= 7):
  painter.goto(0,0)
  painter.setheading((angle)*numLegDrawn/1.7)
  print(angle*(numLegDrawn))
  painter.forward(length)
  numLegDrawn = numLegDrawn + 1
painter.penup()
painter.goto(15,0)
painter.right(90)
painter.pendown()
painter.color("red")
painter.stamp()
painter.penup()
painter.goto(-15, 0)
painter.pendown()
painter.stamp()
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()