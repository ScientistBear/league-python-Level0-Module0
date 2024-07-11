import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
E = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
E.shape('turtle')
# Set your turtle's speed using .speed(2)
E.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
E.color('green')
E.pencolor('black')
# Move your turtle forward using .forward(100)
for i in range(4):
    E.forward(60)
# TEST    Did your turtle move forward?

# Move your turtle left or right using .left(90) or .right(90)
    E.left(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?

# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen

# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?

# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below

# Draw 3 more shapes with different fill colors!

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
