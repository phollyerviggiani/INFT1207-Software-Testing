import unittest # importing unittest
from app.minimum import Minimum # from minimum.py file, import minimum class

class Testminimum(unittest.TestCase): # passing unittest through class
    def setUp(self): # set up function
        self.min_finder = Minimum()
    
    def test_case1(self): # test case 1 function, find.min = inputs, followed byexpected outcome
        self.assertEqual(self.min_finder.find_min([90]), 90)
        self.assertEqual(self.min_finder.find_min([12, 10]), 10)
        self.assertEqual(self.min_finder.find_min([10, 12]), 10)
        self.assertEqual(self.min_finder.find_min([12, 14, 36]), 12)
        self.assertEqual(self.min_finder.find_min([36, 14, 12]), 12)
        self.assertEqual(self.min_finder.find_min([14, 12, 36]), 12)

    def test_case2(self): # test case 2 function for if no input
        with self.assertRaises(ValueError):
            self.min_finder.find_min([])

    def test_case3(self): # test case 3 function, find.min = inputs, followed by expected outcome
        self.assertEqual(self.min_finder.find_min([10, 23, 34, 81, 97]), 10)
        self.assertEqual(self.min_finder.find_min([97, 81, 34, 23, 10]), 10)

    def test_case4(self): # test case 4 function, find.min = inputs, followed by expected outcome
        self.assertEqual(self.min_finder.find_min([10, -2, 5, 23]), -2)
        self.assertEqual(self.min_finder.find_min([10, -2, -24, 4]), -24)
    
    def test_case5(self): # test case 5 function, find.min = inputs, followed by expected outcome
        self.assertEqual(self.min_finder.find_min([-23, -31, -45, -56]), -56)
        self.assertEqual(self.min_finder.find_min([-6, -203, -2, -78]), -203)

    def test_case6(self): # test case 6 function, find.min = inputs, raising TypeError due to float
        with self.assertRaises(TypeError):
            self.min_finder.find_min([23, 34.56, 67, 33])

    def test_case7(self): # test case 7 function, find.min = inputs, raising TypeError due to string
        with self.assertRaises(TypeError):
            self.min_finder.find_min([23, 'hi', 32, 1])
        with self.assertRaises(TypeError):
            self.min_finder.find_min([12, '&', '*', '34m', '!'])
    
    def test_case8(self): # test case 8 function, find.min = inputs, follwed by expected outcome
        self.assertEqual(self.min_finder.find_min([3, 4, 6, 9, 6]), 3)
        self.assertEqual(self.min_finder.find_min([13, 6, 6, 9, 15]), 6)
    
    def test_case9(self): # test case 9 function, find.min = inputs, followed by expected output
        self.assertEqual(self.min_finder.find_min([530, 429449672, 97, 23, 46, 59]), 23)

if __name__ == '__main__':
    unittest.main()