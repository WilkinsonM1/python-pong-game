#Simple Pong game in Python 3

import turtle

#first we need to make a window
wn = turtle.Screen()

#window title
wn.title("Pong by @MohammedWilkinson")

#window background colour
wn.bgcolor("black")

#window size in pixels
wn.setup(width=800, height=600)

#we stop the window from updating
wn.tracer(0)
#we manually update this now, but this helps speed up the game's performance

#Score
score_a = 0
score_b = 0

#Game Objects

#Paddle A
paddle_a = turtle.Turtle()
#small t for module and big T for object name
paddle_a.speed(0) #fastest speed for animation purposes
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #the multiplier that we will stretch the object which by defualt starts at 20 pixels for each dimension
paddle_a.penup() #so that the object doesn't draw a line when it moves
paddle_a.goto(-350, 0)
#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() 
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape('circle')
ball.color('white')
ball.penup() 
ball.goto(0, 0)
ball.dx = 0.2 #d means delta (change) and x is the coordinate
ball.dy = -0.2 #the combination of these two makes the ball move diagonally up right

#Pen
#this is the object that will draw the scores for us
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup() #as the turtle starts at the centre and we will move it to a different position it will draw a line doing that
pen.hideturtle() #we don't want to see the turtle
pen.goto(0, 260)
pen.write('Player A: 0    Player B: 0', align='center', font=('Courier', 24, 'normal'))


#Functions
def paddle_a_up(): # to create a function we use keyword def (define) and then colon after parantheses
    y =  paddle_a.ycor() 
    #returns the y-coordinate of object and stores it in y
    y += 20
    #adds 20 pixels to y
    paddle_a.sety(y)
    #sets paddle_a's y to the new y

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up(): 
    y =  paddle_b.ycor() 
    y += 20
    paddle_b.sety(y)
  

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#now we need to call the function once we have defined it by binding it to keyboard buttons
#Keyboard binding
wn.listen() #need to write this to listen for keyboard inputs
wn.onkeypress(paddle_a_up, 'w') #takes function as first parameter and keyboard button as second parameter which must be lowercase
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up') #the arrow keys are named by their direction but the first letter is capitalised
wn.onkeypress(paddle_b_down, 'Down')


#Main game loop
#the meat and potatoes of our game is here
while True:
    wn.update() 
    #every time the program runs a loop it will update

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #sets the coordinates to the current position plus the new position

    #Border checking
    #top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    #if the current y coordinate of ball is greater than 290 then set it back to 290 and reverse the y direction by timesing it by -1
    #bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A: {}    Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))
    #if ball goes off screen to the right then goes back to the center and moves in the opposite direction
    #and player A gets 1 point
    #{} is for printing and the format function puts its first parameter in the first curly braces and the second parameter in the second curly braces
    #the clear function gets rid of what's printed otherwise the scores will just be written over each other
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {}    Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1
    #essentially when the ball's x coordinate crosses the paddle and the ball is within the length of the paddle then it gets reversed or "bounced"
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1
