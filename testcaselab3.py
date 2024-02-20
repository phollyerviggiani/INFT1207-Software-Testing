import unittest
from lab3 import circle_area, trapezium

class testshapes(unittest.TestCase):
    def test_circle(self):
        self.assertAlmostEqual(circle_area(5), second= 78.54, places= 2)
        self.assertAlmostEqual(circle_area(0), second= 0, places= 2) # places = rounding up
    
    def test_trapezium(self):
        self.assertAlmostEqual(trapezium(5, 7, 4), second= 24, places= 2)