import math # importing math functionality for pi

class Shape_Calculator: # creating Shape_Calculator class
    def circle_area(self, radius): # defining funtion for circle area calculation
        if radius < 0: # checking is numbers are above 0
            raise ValueError("Radius must be greater than or equal to 0.")
        return math.pi * radius**2 # passing self and radius

    def trapezium_area(self, base1, base2, height): # defining funtion for trapezium area calculation
        if base1 < 0 or base2 < 0 or height < 0: # checking is numbers are above 0
            raise ValueError("Base lengths and height must be greater than or equal to 0.")
        return 0.5 * (base1 + base2) * height # passing self, base1, base2, and height

    def ellipse_area(self, axis1, axis2): # defining ellipse_area function
        if axis1 < 0 or axis2 < 0: # checking is numbers are above 0
            raise ValueError("The Axis must be greater than or equal to 0.")
        return math.pi * axis1 * axis2 # passing self, axis1, and axis2

    def rhombus_area(self, p, q): # defining rhombus_area function
        if p < 0 or q < 0: # checking is numbers are above 0
            raise ValueError("The values p and q must be greater or equal to 0.") 
        return 0.5 * p * q # passing p and q 