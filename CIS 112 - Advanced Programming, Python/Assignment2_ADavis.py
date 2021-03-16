'''
This assignment has Python Turtle draw concentric squares
'''

import turtle

# Get screen for turtle and get turtle
s = turtle.getscreen() # pylint: disable = maybe-no-member
t = turtle.getturtle() # pylint: disable = maybe-no-member

# Length of the side
side = 120
# Subtraction value to get smaller sides
sub = 20

# Turtle loop
while side > 0:
    for _ in range(4):
        t.fd(side)
        t.rt(90)
    t.penup()
    t.fd(sub/2)
    t.rt(90)
    t.fd(sub/2)
    t.lt(90)
    t.pendown()
    side -= sub

# Keeps output screen alive to see the drawing
input('Press enter to exit')