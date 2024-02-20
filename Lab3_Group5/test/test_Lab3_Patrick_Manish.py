import unittest # importing unittest
from app.Lab3_Patrick_Manish import Shape_Calculator # from FIX AFTER FINAL NAME, file, importing the Shape_Calculator class

class testshapes(unittest.TestCase): # making a class - unittest 
    def setUp(self): # set up function, assigning Shape_Calculator class
        self.calculator = Shape_Calculator()
    
    def test_circle_1(self): # testing area of circle
        self.assertAlmostEqual(self.calculator.circle_area(5), second= 78.54, places= 2)
        self.assertAlmostEqual(self.calculator.circle_area(0), second= 0, places= 2)
        self.assertAlmostEqual(self.calculator.circle_area(14.3), second= 642.42, places= 2)
        self.assertAlmostEqual(self.calculator.circle_area(2), second= 12.57, places= 2)
    
    def test_circle_2(self): # testing circle: entering a string
        with self.assertRaises(TypeError):
            self.calculator.circle_area('ten')
    
    def test_circle_3(self): # testing circle: entering negative
        with self.assertRaises(ValueError):
            self.calculator.circle_area(-5)
    
    def test_trapezium_1(self): # testing area of trapezium
        self.assertAlmostEqual(self.calculator.trapezium_area(5, 7, 4), second= 24.00, places= 2)
        self.assertAlmostEqual(self.calculator.trapezium_area(1, 3, 5), second= 10.00, places= 2)
    
    def test_trapezium_2(self): # testing area of trapezium: entering string
        with self.assertRaises(TypeError):
            self.calculator.trapezium_area('ten', -4, 'hello')
    
    def test_trapezium_3(self): # testing area of trapezium: entering negatives
        with self.assertRaises(ValueError):
            self.calculator.trapezium_area(-9, 2, -5)
        
    def test_ellipse_1(self): # testing area of ellipse
        self.assertAlmostEqual(self.calculator.ellipse_area(4, 3), second= 37.70, places=2)
        self.assertAlmostEqual(self.calculator.ellipse_area(2, 2), second= 12.57, places=2)
        self.assertAlmostEqual(self.calculator.ellipse_area(32, 86), second= 8645.66, places=2)
    
    def test_ellipse_2(self): # testing area of ellipse: entering decimals
        self.assertAlmostEqual(self.calculator.ellipse_area(8.5, 6.7), second= 178.91, places=2)
    
    def test_ellipse_3(self): # testing area of ellipse: entering string
        with self.assertRaises(TypeError):
            self.calculator.ellipse_area('fifteen', 'thirty')
            
    def test_ellipse_4(self): # testing area of ellipse: entering negatives
        with self.assertRaises(ValueError):
            self.calculator.ellipse_area(-20, -54.5)

    def test_rhombus_1(self): # testing area of rhombus
        self.assertAlmostEqual(self.calculator.rhombus_area(6, 8), second= 24.0, places=2)
    
    def test_rhombus_2(self): # testing area of rhombus with decimals
        self.assertAlmostEqual(self.calculator.rhombus_area(3.6, 8.8), second= 15.84, places=2)
    
    def test_rhombus_3(self): # testing area of rhombus: entering string
        with self.assertRaises(TypeError):
            self.calculator.rhombus_area('twelve', 'hi')
    
    def test_rhombus_4(self):
        with self.assertRaises(ValueError): # testing area of a rhombus: entering negative
            self.calculator.rhombus_area(-7, -14.65)
        
def suite(): # test suite, allowing to choose which test case we want to test.
    while True:
        print("Please enter one of the following options: ")
        print(" - 'c' for testing area of circle")
        print(" - 't' for testing area of trapezium")
        print(" - 'e' for testing area of ellipse")
        print(" - 'r' for testing area of rhombus")
        print(" - 'q' to quit")
        choice = input("\nWhat would you like to do?: ").lower()
        suite = unittest.TestSuite()
        
        if choice == 'c': # tests the circle
            suite.addTest(testshapes('test_circle_1'))
            suite.addTest(testshapes('test_circle_2'))
            suite.addTest(testshapes('test_circle_3'))
            return suite
        
        elif choice == 't': # tests the trapezium
            suite.addTest(testshapes('test_trapezium_1'))
            suite.addTest(testshapes('test_trapezium_2'))
            suite.addTest(testshapes('test_trapezium_3'))
            return suite
        
        elif choice == 'e': # tests the ellipse
            suite.addTest(testshapes('test_ellipse_1'))
            suite.addTest(testshapes('test_ellipse_2'))
            suite.addTest(testshapes('test_ellipse_3'))
            suite.addTest(testshapes('test_ellipse_4'))
            return suite
        
        elif choice == 'r': # tests the rhombus
            suite.addTest(testshapes('test_rhombus_1'))
            suite.addTest(testshapes('test_rhombus_2'))
            suite.addTest(testshapes('test_rhombus_3'))
            suite.addTest(testshapes('test_rhombus_4'))
            return suite
        
        elif choice == 'q': # exits the program
            quit()
            
        else: # if user inputs wrongly, prompt for input again
            print("Please enter either c, t, e, r, or q.")
        
if __name__ == '__main__': # checking to see if file match
    while True: # while true, assign test suite function to the variable
        test_suite = suite()
        if test_suite: # if there is test suite, make a runner, passing it through test suite
            runner = unittest.TextTestRunner()
            runner.run(test_suite)
        else: # if not, break loop, exiting program
            break