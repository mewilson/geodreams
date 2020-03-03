import turtle as t
import numpy as np
import math
import shapelib


# GLOBAL VARIABLES
EDGE_NUM = 3
RADIUS = 30

# center_agent = t.Turtle()

agent = t.Turtle()
agent.hideturtle()
agent.speed("fastest")
agent.radians()

for i in range(3, 20):
    shapelib.draw_shape(agent, i, 100)

#for i in np.arange(10, 100, 10):
#    shapelib.draw_shape(agent, 100 * i, i)


t.exitonclick()
    
    
    
    
