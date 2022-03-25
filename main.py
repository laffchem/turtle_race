from email.errors import MisplacedEnvelopeHeaderDefect
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your bet!", prompt="Which turtle will win the race? Enter a color (red, yellow, green, orange, purple, blue): ")
print(user_bet)

is_race_on = False


jim = Turtle()
jim.shape("turtle")
jim.color("yellow")

tim = Turtle()
tim.shape("turtle")
tim.color("green")

raphael = Turtle()
raphael.shape("turtle")
raphael.color("red")

michaelangelo = Turtle()
michaelangelo.shape("turtle")
michaelangelo.color("orange")

donatello = Turtle()
donatello.shape("turtle")
donatello.color("purple")

leonardo = Turtle()
leonardo.shape("turtle")
leonardo.color("blue")

#I am aware I could've done a for loop for all of the previous code and the list, but I wanted to name them after TMNT.
all_turtles = [jim, tim, raphael, michaelangelo, donatello, leonardo]

def race_start():
    jim.penup()
    jim.goto(-230, -167)
    tim.penup()
    tim.goto(-230, -100)
    raphael.penup()
    raphael.goto(-230, -33)
    michaelangelo.penup()
    michaelangelo.goto(-230, 33)
    donatello.penup()
    donatello.goto(-230, 100)
    leonardo.penup()
    leonardo.goto(-230, 167)

# If the user has bet, start the race. Vroom vroom!
if user_bet:
    is_race_on=True
race_start()


#The code for the race. The screen being 500 wide, when the turtle which is a 40 x 40 object crosses 250 - (40/2) which is 230, the race is over.

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle is the winner")
            else:
                print(f"You've lost! The {win_color} turtle is the winner!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
    

screen.exitonclick()