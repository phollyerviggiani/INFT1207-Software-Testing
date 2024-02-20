import unittest
def add(x,y):
    return x + y
    #you can execute the program or right click and execute unit test for this
class SimpleTest(unittest.TestCase):
    def testadd1(self): #self represents the instance of the class.
# By using the “self” keyword we can access the attributes and methods of
# the class in python.
        self.assertEqual(add(4,5),9)
if __name__ == '__main__':
    unittest.main()