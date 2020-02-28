import turtle as t
import numpy as np

t.hideturtle()

half_width = 300
half_height = 300

divisions = 30

def putAt(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()

# Draw axis
putAt(-1 * half_width, half_height)
t.goto(-1 * half_width, -1 * half_height)
t.goto(half_width, -1 * half_height)

# Start at right bottom corner and draw to left
putAt(half_width, -1 * half_height)

for i in np.arange(0, half_width * 2 + (half_width * 2 / divisions), half_width * 2 / divisions):
    t.goto(-1 * half_width, -1 * half_height + i)
    putAt(half_width - i, -1 * half_height)
    
    
# Start at left top corner and down

#t.goto(-300, 300)
#
#for i in np.arange(0, 660, 60):
#    t.goto(-300 + i, -300)
#    t.goto(-300, 300 - i)

while(True):
    t.left(0)

