import turtle as t
import geoLib
import numpy as np

def v(x, y):
    return t.Vec2D(x, y)

def make_gradients(agents, x, y, div):

    # For every line drawn in a curve.
    for i in np.arange(0, div):

        # Calculate the change from the original dimensions.
        dx = i * (x * 2 / div)
        dy = i * (y * 2 / div)
        
        # Calculate the origins and destinations of this movement.
        origins = [v(x, y - dy),
                   v(x - dx, -1 * y),
                   v(-1 * x, (-1 * y) + dy),
                   v((-1 * x) + dx, y)]

        # Destinations are the same as origins but shifted one to the left.
        dests= [v(x - dx, -1 * y),
                v(-1 * x, -1 * y + dy),
                v(-1 * x + dx, y),
                v(x, y - dy)]
        
        # Have each agent draw its line.
        for i in range(len(agents)):
            geoLib.pa(agents[i], origins[i])
            agents[i].goto(dests[i])
                

def main():
    
    # Define the team of agents.
    upperRight = t.Turtle()
    lowerRight = t.Turtle()
    lowerLeft = t.Turtle()
    upperLeft = t.Turtle()

    agents = [upperRight, lowerRight, lowerLeft, upperLeft]
    
    # Hide all agents and set their speed.
    geoLib.hide_all(agents)
    geoLib.set_speed(agents)
    
    # Draw the figure.
    make_gradients(agents, 300, 300, 30)
    
    t.exitonclick()
    
if __name__ == '__main__':
    main()
