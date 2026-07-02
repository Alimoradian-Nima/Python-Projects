import turtle
import winsound # for adding sound

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600) #windows size  # center 0.0 +-300h  +-400w  
win.tracer(0) #stops window from updating == smoother game

# paddle a
paddle_a = turtle.Turtle()  # module . class
paddle_a.speed(0) #max speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5 , stretch_len=1) #5*20 
paddle_a.penup() # no trace lines
paddle_a.goto(-350,0)

#paddle b
paddle_b = turtle.Turtle()  # module . class
paddle_b.speed(0) #max speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5 , stretch_len=1) #5*20 
paddle_b.penup()
paddle_b.goto(+350,0)

# border a
b_a = turtle.Turtle()  # module . class
b_a.shape("square")
b_a.color("red")
b_a.shapesize(stretch_wid=30 , stretch_len=1/20) #30*20 1/20*20
b_a.penup()
b_a.goto(-400,0)

#border b
b_b = turtle.Turtle()  # module . class
b_b.shape("square")
b_b.color("red")
b_b.shapesize(stretch_wid=30 , stretch_len=1/20) #30*20 1/20*20
b_b.penup()
b_b.goto(+400,0)

#border x
b_x = turtle.Turtle()  # module . class
b_x.shape("square")
b_x.color("blue")
b_x.shapesize(stretch_wid=1/20 , stretch_len=40) # 1/20*20  40*20
b_x.penup()
b_x.goto(0,300)

#border y
b_y = turtle.Turtle()  # module . class
b_y.shape("square")
b_y.color("blue")
b_y.shapesize(stretch_wid=1/20 , stretch_len=40) # 1/20*20  40*20
b_y.penup()
b_y.goto(0,-300)

# ball
ball = turtle.Turtle()  # module . class
ball.speed(0) #max speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2 # dx == change
ball.dy = 0.2

#score
score_a=0
score_b=0

# pen
pen = turtle.Turtle()
pen.speed (0) #animation speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,240)
pen.write("A "+ str(score_a) +" : "+ str(score_b) +" B", align="center" , font=("courier",24,"normal"))

#functions
def paddle_a_up() :
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down() :
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up() :
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down() :
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def paddle_a_right() :
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)
    
def paddle_a_left() :
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)

# keyboard binding
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_a_right,"d") #test
win.onkeypress(paddle_a_left,"a") #test
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")

# Main game loop
while True:
    win.update()

    # ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # ball borders 
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
        #winsound.PlaySound("sound.wav", winsound.SND_ASYNC) # adding sounds from sysytem files

    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1    

    if ball.xcor() > 390 :
        # ball.setx(390)
        # ball.dx *= -1
        score_a += 1
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        pen.write("A "+ str(score_a) +" : "+ str(score_b) +" B", align="center" , font=("courier",24,"normal"))


    if ball.xcor() < -390 :
        # ball.setx(-390)
        # ball.dx *= -1
        score_b += 1
        ball.goto(0,0)
        ball.dx *= -1
        ball.dy *= -1
        pen.clear()
        pen.write("A "+ str(score_a) +" : "+ str(score_b) +" B", align="center" , font=("courier",24,"normal"))


    # ball and paddle
    if (ball.xcor() > 340 and ball.xcor()< 350) and (ball.ycor() < paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor() -50) :
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < paddle_a.xcor() +10 and ball.xcor()> paddle_a.xcor()) and (ball.ycor() < paddle_a.ycor() +50 and ball.ycor() > paddle_a.ycor() -50) :
        ball.setx(paddle_a.xcor()+10)
        ball.dx *= -1

