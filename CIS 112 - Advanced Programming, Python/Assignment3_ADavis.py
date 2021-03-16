'''
This assignment has Python Turtle draw a user defined polygon in a repeated circle as well as in a scaled drawing
'''

import turtle

# Determines the polygon angles based on number of sides
def angle(sides):
    angle = (180 * (sides - 2)) / sides
    return 180-angle

# Draws the polygon
def drawShape(Turtle, sides, length):
    a = angle(sides)
    for _ in range(sides):
        Turtle.fd(length)
        Turtle.lt(a)

# Repeat polygon in a spinning circle
def SpinPolygon(Turtle, sides, angle, length, repeat):
    for _ in range(repeat):
        drawShape(Turtle, sides, length)
        Turtle.lt(360/repeat)

# Draws number of polygons with increasing scale
def ScalePolygon(Turtle, sides, length, sfactor, number):
    for _ in range(number):
        drawShape(Turtle, sides, length)
        length *= sfactor

# Set up variables
side = int(input('Please enter how many sides you want in your polygon (> 3): '))
l = int(input('Please enter the length of your sides: '))
r = int(input('Please enter the number of times to repeat the polygon: '))
scale = float(input('Please enter the scale factor: '))

# Turtle starting position
# turtle.speed(20) # pylint: disable = maybe-no-member
turtle.penup() # pylint: disable = maybe-no-member
turtle.rt(180) # pylint: disable = maybe-no-member
turtle.fd(300) # pylint: disable = maybe-no-member
turtle.rt(180) # pylint: disable = maybe-no-member
turtle.pendown() # pylint: disable = maybe-no-member

# Draw first set of drawings
SpinPolygon(turtle, side, angle(side), l, r)

# Move Turtle to prep for second drawing
turtle.setheading(315) # pylint: disable = maybe-no-member
turtle.penup() # pylint: disable = maybe-no-member
turtle.fd(400) # pylint: disable = maybe-no-member
turtle.setheading(0) # pylint: disable = maybe-no-member
turtle.fd(100) # pylint: disable = maybe-no-member
turtle.pendown() # pylint: disable = maybe-no-member

# Draw second set of drawings
ScalePolygon(turtle, side, l, scale, r)

# Keeps output screen alive to see the drawing
input('Press enter to exit')