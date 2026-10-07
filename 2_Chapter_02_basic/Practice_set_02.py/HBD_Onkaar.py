import turtle
import time
import random

# Setup screen
screen = turtle.Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("Black")
screen.title("Happy Birthday Dear Onkar!")

# Helper function for drawing text
def draw_text(message, x, y, font_size, color):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.write(message, align="center", font=("Comic Sans MS", font_size, "bold"))

# Function to draw a cake
def draw_cake():
    cake = turtle.Turtle()
    cake.hideturtle()
    cake.penup()
    cake.goto(-100, -150)
    cake.color("chocolate")
    cake.pendown()
    cake.begin_fill()
    for _ in range(2):
        cake.forward(200)
        cake.left(90)
        cake.forward(100)
        cake.left(90)
    cake.end_fill()
    
    # Add frosting
    cake.color("Darkpink")
    cake.penup()
    cake.goto(-110, -50)
    cake.pendown()
    cake.begin_fill()
    for _ in range(2):
        cake.forward(220)
        cake.left(90)
        cake.forward(20)
        cake.left(90)
    cake.end_fill()
    
    # Add candles
    cake.penup()
    cake.goto(-80, -30)
    for i in range(5):
        cake.color("yellow")
        cake.pendown()
        cake.begin_fill()
        cake.forward(10)
        cake.left(90)
        cake.forward(30)
        cake.left(90)
        cake.forward(10)
        cake.left(90)
        cake.forward(30)
        cake.left(90)
        cake.end_fill()
        cake.penup()
        cake.forward(40)

# Function to draw balloons
def draw_balloon(x, y, color):
    balloon = turtle.Turtle()
    balloon.penup()
    balloon.shape("circle")
    balloon.color(color)
    balloon.goto(x, y)
    balloon.speed(1)
    for _ in range(50):
        balloon.sety(balloon.ycor() + 2)
        time.sleep(0.05)
    balloon.hideturtle()

# Draw a boy character
def draw_boy():
    boy = turtle.Turtle()
    boy.speed(5)
    boy.penup()
    boy.hideturtle()

    # Draw head
    boy.goto(-300, -100)
    boy.color("tan")
    boy.pendown()
    boy.begin_fill()
    boy.circle(30)
    boy.end_fill()

    # Draw body
    boy.penup()
    boy.goto(-300, -130)
    boy.pendown()
    boy.color("white")
    boy.begin_fill()
    for _ in range(2):
        boy.forward(60)
        boy.right(90)
        boy.forward(80)
        boy.right(90)
    boy.end_fill()

    # Draw pants
    boy.color("black")
    boy.begin_fill()
    for _ in range(2):
        boy.forward(60)
        boy.left(90)
        boy.forward(40)
        boy.left(90)
    boy.end_fill()

    # Return the turtle for animation
    return boy

# Function to animate the boy cutting the cake
def animate_boy(boy):
    # Move boy to the cake
    for _ in range(30):
        boy.setx(boy.xcor() + 10)
        time.sleep(0.05)

    # Pretend to cut the cake
    boy.setheading(-90)
    boy.forward(50)
    time.sleep(0.5)
    boy.backward(50)

    # Display thank you message
    draw_text("Thank you!", 0, -300, 28, "dark red")

# Main function to combine everything
def main():
    # Display birthday message
    draw_text("Wishing You a Very", 0, 200, 24, "blue")
    draw_text("Happy Birthday Onkar!", 0, 160, 32, "red")
    
    # Draw cake
    draw_cake()
    
    # Create animated balloons
    colors = ["red", "yellow", "blue", "green", "purple"]
    for _ in range(8):
        x = random.randint(-300, 300)
        y = random.randint(-300, -200)
        draw_balloon(x, y, random.choice(colors))
      
    # End program
    turtle.done()

if __name__ == "__main__":
    main()

        