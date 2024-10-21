

#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
wn = trtl.Screen()
wn.screensize(canvwidth = .75, canvheight = .75)

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
  

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions
extraSpeedH = 1
extraSpeedV = 0
for i in range(50):
    for ht in horiz_turtles:
       ht.forward(4 + extraSpeedH)
    if (abs(ht.xcor() - vt.xcor()) < 10):
            vert_turtles.remove(vt)
            ht.right(360)
            ht.forward(-40)
            horiz_turtles.append(ht)
    for vt in vert_turtles:
       vt.forward(4 + extraSpeedV)
    if (abs(ht.ycor() - vt.ycor()) < 10):
            horiz_turtles.remove(ht)
            vt.left(360)
            vt.forward(-40)
            vert_turtles.append(vt)
    extraSpeedH += 2
    extraSpeedV += 1.3
    if extraSpeedH >= 10:
         extraSpeedH = -1
    if extraSpeedV >= 12:
         extraSpeedV = 2




'''




###### code segment #####



###### code segment #####

 

###### code segment #####
 
 

'''

wn.mainloop()