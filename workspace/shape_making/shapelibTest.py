import turtle as t
import shapelib
import math

import unittest

class Testgeolib(unittest.TestCase):

    def test_print(self):
    
        self.assertEqual(shapelib.test_print(), "This is ShapeLib.")

    def test_calc_vertex_angle(self):
    
        # Triangle
        actual = round(shapelib.calc_vertex_angle(3), 2)
        expected = round(math.pi / 3, 2)
        self.assertEqual(actual, expected)
        
        # Square
        actual = round(shapelib.calc_vertex_angle(4), 2)
        expected = round(math.pi / 2, 2)
        self.assertEqual(actual, expected)
        
        # Pentagon
        actual = round(shapelib.calc_vertex_angle(5), 2)
        expected = round(1.8849555921538759, 2)
        self.assertEqual(actual, expected)
        

    def test_calc_side_len(self):
    
        len = round(shapelib.calc_side_len(3, 2), 2)

        self.assertEqual(len, round(3.4641016151377544, 2))
    

if __name__ == '__main__':
    unittest.main()
