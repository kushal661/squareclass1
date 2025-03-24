import turtle
import random
from selectors import SelectSelector

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('black')

t=turtle.Turtle()
#code in here
#menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('white')
t.write("Background color",font=("Arial",30,"normal"),align="center")

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor('tan')
t.write("1. Tan",font=("Arial",20,"normal"),align="left")

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor('Azure')
t.write("2. Azure",font=("Arial",20,"normal"),align="left")

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor('Aquamarine')
t.write("3. Aquamarine",font=("Arial",20,"normal"),align="left")

t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor('Darkkhaki')
t.write("4. Darkkhaki",font=("Arial",20,"normal"),align="left")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor('White')
t.write("Choose a Color",font=("Arial",30,"normal"),align="Center")

choice = int(input("Choose a Color: "))
if choice == 1:
    screen.bgcolor('tan')

elif choice == 2:
    screen.bgcolor('azure')

elif choice == 3:
    screen.bgcolor('aquamarine')

elif choice == 4:
    screen.bgcolor('darkkhai')
t.clear()
#enter your name
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('Black')
t.write("Enter Your Name",font=("Arial",30,"normal"),align="Center")

name = input("Enter your name: ")
t.clear()
operation = random.randint(1,4)
if operation == 1:
    symbol = "+"
    #add
    #num1 = int(input("Enter a number: "))
    #num2 = int(input("Enter another number: "))
    num1 = random.randint(-100,100)
    num2 = random.randint(-100,100)
    solution = num1 + num2
elif operation == 2:
    symbol = "-"
    #subtract
    num1 = random.randint(-100,100)
    num2 = random.randint(-100,100)
    solution = num1 - num2
elif operation == 3:
    symbol = "*"
     #multiply
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)
    solution = num1 * num2
elif operation == 4:
    symbol = "/"
     #divide
    num1 = random.randint(-10, 10)
    num2 = random.randint(1, 10)
    sign = random.randint(1,2)
    if sign == 2:
        num2 = -1*num2
    solution = num1 - num2
#move
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('blue')
t.write(name,font=("Arial",30,"normal"),align="center")

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor('blue')
t.write(num1,font=("Arial",30,"normal"),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor('blue')
t.write(symbol,font=("Arial",30,"normal"),align="center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('blue')
t.write(num2,font=("Arial",30,"normal"),align="center")

t.penup()
t.goto(100,0)
t.pendown()
t.pencolor('blue')
t.write("=",font=("Arial",30,"normal"),align="center")

answer = float(input("Enter the answer: "))

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor('blue')
t.write(solution,font=("Arial",30,"normal"),align="center")


t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('black')
t.write("your answer: "+str(answer),font=("Arial",30,"normal"),align="center")

if answer == solution:
    screen.bgcolor('dodgerblue')


    t.penup()
    t.goto(0,100)
    t.pendown()
    t.pencolor('black')
    t.write("Good Job",font=("Arial",30,"normal"),align="center")
else:
    screen.bgcolor('darkorange')
    t.penup()
    t.goto(0,100)
    t.pendown()
    t.pencolor('black')
    t.write("Wrong",font=("Arial",30,"normal"),align="center")

turtle.done()

