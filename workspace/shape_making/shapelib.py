import numpy as np
import math
import turtle as t
import geolib

def test_print():
    print ("This is ShapeLib.")
    return "This is ShapeLib."

def calc_side_len(num_edges, radius):

    return math.sin(math.pi / num_edges) * 2 * radius
    
    
#def calc_vertex_angle(num_edges):
#
#    return math.pi * (num_edges - 2)
    
    
def calc_vertex_angle(num_edges):

    internal_angle = 2 * math.pi / num_edges
    external_angle = math.pi - internal_angle

    return external_angle
    
    
def draw_shape(agent, num_edges, radius, start_point = t.Vec2D(0, 0)):

    side_len = calc_side_len(num_edges, radius)
    
    vertex_angle = calc_vertex_angle(num_edges)

    # Go to first vertex
    # geolib.pa(agent, start_point + t.Vec2D(radius, 0))
    
    for i in range(num_edges):
        # Turn
        agent.lt(math.pi - vertex_angle)
        agent.fd(side_len)
    
    

