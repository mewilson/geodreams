import turtle as t
import math

# Find teh distance between to points.
def dist(vec1, vec2):
    diff = vec1 - vec2

    return math.sqrt( diff[0]**2 + diff[1]**2 )


# Put an agent at a specific point without drawing.
def pa(agent, vec):
    agent.pu()
    agent.goto(vec)
    agent.pd()


# Put an agent at a specific point without drawing.
def put_at(agent, vec):
    agent.pu()
    agent.goto(vec)
    agent.pd()
    
# Calculate change in x and y for a single step in a multi-step process.
def calc_step(origin, dest, steps):

    x_step = (dest[0] - origin[0]) / steps
    y_step = (dest[1] - origin[1]) / steps

    return t.Vec2D(x_step, y_step)
    

# Move one agent in some amount of steps.
def mv(agent, vec, steps):

    step = calc_step(agent.pos(), vec, steps)

    for i in range(steps):
        agent.goto(agent.pos() + step)

 
# Move a team of agents in some amount of steps.
def mv_team(agent_arr, origin_arr, dest_arr, steps):

    if len(agent_arr) != len(origin_arr) or len(agent_arr) != len(dest_arr):
        raise IndexError("agent and vec array are of unequal lengths.")

    num_agents = len(agent_arr)
    
    # Move all agents to their origin
    for i in range(num_agents):
        put_at(agent_arr[i], origin_arr[i])

    # Calculate the step distance.
    step_arr = [calc_step(origin_arr[i], dest_arr[i], steps) for i in range(num_agents)]
    
    # Move all agents to their destination.
    for i in range(steps):
        for j in range(num_agents):
            agent_arr[j].goto(agent_arr[j].pos() + step_arr[j])
            

# Make a square in some amount of steps.
def make_square(agents, x_dim, y_dim, steps):

    # Origins are the corners of which the turtles start.
    origins = [t.Vec2D(x_dim, y_dim), t.Vec2D(x_dim, -1 * y_dim), t.Vec2D(-1 * x_dim, -1 * y_dim), t.Vec2D(-1 * x_dim, y_dim)]

    # Destinations are the same as origins but shifted one to the left.
    dests= [t.Vec2D(x_dim, -1 * y_dim), t.Vec2D(-1 * x_dim, -1 * y_dim), t.Vec2D(-1 * x_dim, y_dim), t.Vec2D(x_dim, y_dim)]

    mv_team(agents, origins, dests, steps)

    
# Clear drawings of all agents.
def clear_all(agents):

    for agent in agents:
        agent.undo()
      

# Hides all agents.
def hide_all(agents):

    for agent in agents:
        agent.hideturtle()
   

# Sets speed for all agents.
def set_speed(agents, speed = "fastest"):

    for agent in agents:
        agent.speed(speed)
    
    

    
    
