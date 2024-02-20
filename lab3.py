import math
def circle_area(radius):
    return math.pi * radius**2

def trapezium(base1, base2, height):
    return 0.5 * (base1 + base2) * height

choice = input("1, 2 or 3")
if choice == 1:
    radius = input("Enter radius")

if choice == 2:
    trapezoidbase1 = input("Enter Base 1: ")
    trapezoidbase2 = input("Enter Base 2: ")
    trapezoidheight = input("Enter Height: ")
