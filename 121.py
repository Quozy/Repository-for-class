# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
t = trtl.Turtle()
wn = trtl.Screen()



#-----game configuration----

t.fillcolor("green")
t.shape("triangle")
t.shapesize(3)
t.penup()
score = 0
#-----initialize turtle-----

scoreWriter = trtl.Turtle()
scoreWriter.hideturtle()
scoreWriter.penup()
scoreWriter.goto(-275, 250)
fontSetup = ("Arial", 20, "normal")
#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(250,250)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

wn.ontimer(countdown, counter_interval) 


#-----game functions--------
def spot_clicked(x,y):
    if timer_up == True:
       t.hideturtle()
    else:
        changePosition()
        updateScore()
def changePosition():
    newXPos = rand.randint(-300,300)
    newYPos = rand.randint(-200,200)
    t.goto(newXPos, newYPos)
def updateScore():
    global score
    score = score + 1 
    scoreWriter.clear()
    scoreWriter.write(score, font=fontSetup)
#-----events----------------
t.onclick(spot_clicked)




wn.mainloop()