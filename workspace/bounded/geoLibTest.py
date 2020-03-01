import turtle as t
import geoLib

import unittest

class TestGeoLib(unittest.TestCase):

    def test_dist(self):
        
        vec1 = t.Vec2D(0, 0)
        vec2 = t.Vec2D(3, 4)
        
        actual = geoLib.dist(vec1, vec2)
    
        self.assertEqual(round(actual, 2), 5.00)

    def test_pa(self):
    
        agent = t.Turtle()
        expected = t.Vec2D(5, 10)
        geoLib.pa(agent, expected)
        
        self.assertEqual(agent.pos(), expected)
        
    def test_mt(self):
    
        agent = t.Turtle()
        
        # First Quadrant
        expected = t.Vec2D(5, 10)
        geoLib.mt(agent, expected, 20)
        
        self.assertEqual(agent.pos(), expected)
        
        # Second Quadrant
        expected = t.Vec2D(-50, 110)
        geoLib.mt(agent, expected, 20)

        self.assertEqual(agent.pos(), expected)
        
        # Third Quadrant
        expected = t.Vec2D(-10, -20)
        geoLib.mt(agent, expected, 20)

        self.assertEqual(agent.pos(), expected)
        
        # Fourth Quadrant
        expected = t.Vec2D(20, -120)
        geoLib.mt(agent, expected, 20)

        self.assertEqual(agent.pos(), expected)
        
    # Make square
    def test_mt_team(self):
    
        # Define the team of agents.
        upperRight = t.Turtle()
        lowerRight = t.Turtle()
        lowerLeft = t.Turtle()
        upperLeft = t.Turtle()

        agents = [upperRight, lowerRight, lowerLeft, upperLeft]
        
        geoLib.hide_all(agents)
        geoLib.set_speed(agents)
        
        
        # Define their starting positions
        origins = [t.Vec2D(300, 300), t.Vec2D(300, -300), t.Vec2D(-300, -300), t.Vec2D(-300, 300)]
        dests= [t.Vec2D(300, -300), t.Vec2D(-300, -300), t.Vec2D(-300, 300), t.Vec2D(300, 300)]
        
        # Move.
        geoLib.mt_team(agents, origins, dests, 100)

if __name__ == '__main__':
    unittest.main()

