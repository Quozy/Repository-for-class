#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)
l = 6
length = 70
z = 380 / l
print(z)
painter.pensize(5)
n = 0
while (n < l):
  painter.goto(0,0)
  painter.setheading(z*n)
  print(z*n)
  painter.forward(length)
  n = n + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()