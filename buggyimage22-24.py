#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used

# Draw Body
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)

# Configure Spider Legs
l = 6
length = 70
angle = 380 / l
print(angle)
painter.pensize(5)
numLegDrawn = 0

# Draw Spider Legs
while (numLegDrawn < l):
  painter.goto(0,0)
  painter.setheading(angle*numLegDrawn)
  print(angle*numLegDrawn)
  painter.forward(length)
  numLegDrawn = numLegDrawn + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()