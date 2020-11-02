# exercise 6
#  geometrie, slope

import math 

def main(): 
    print("This program calculates the slope of a line through two points.")
    print()

    x1 = float(input("Enter the x coordinate of the first point: "))
    y1 = float(input("Enter the y coordinate of the first point: "))
    x2 = float(input("Enter the x coordinate of the second point: "))
    y2 = float(input("Enter the y coordinate of the second point: "))

    slope = (y2-y1)/(x2-x1)

    print("The slope of these two points is: ", slope)

main()
