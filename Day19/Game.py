from turtle import Turtle, Screen
import random
race_on = False
screen = Screen()
screen.setup(width=500,height=400)
colors = ["red","yellow","green","purple","blue","orange"]
y_positions = [-70,-40,-10,20,50,80]
all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtle.append(new_turtle)
user_bet = screen.textinput(title="Make Your Bet!",prompt="Which turtle win the race? Enter a color:-")

if user_bet :
    race_on = True

while race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win! The {winning_color} turtle is winner!")
            else:
                print(f"You Lose! The {winning_color} turtle is winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()