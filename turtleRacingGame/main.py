import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
print_usrInpt = screen.textinput(title="Make your bet", prompt="Which turtle win the race?Enter your color:")
colors = ["red", "green", "yellow", "orange", "blue", "purple"]
turtles_positions = [-70, -40, -10, 20, 50, 80]
all_turtle=[]
user_turtle_exit = False
for turtle_index in range(0, 6):
    new_turtles = Turtle(shape="turtle")
    new_turtles.penup()
    new_turtles.color(colors[turtle_index])
    new_turtles.goto(x=-230, y=turtles_positions[turtle_index])
    all_turtle.append(new_turtles)

if print_usrInpt:
    user_turtle_exit=True

while user_turtle_exit:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            user_turtle_exit=False
            winning_turtle_color=turtle.pencolor()
            if winning_turtle_color==print_usrInpt:
                print(f"Your {winning_turtle_color} color turtle have won the race :)")
            else:
                print(f"Your turtle have lost the race  :(")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()
