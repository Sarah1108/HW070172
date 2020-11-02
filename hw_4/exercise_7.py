# exercise 7
#   geometrie, distance between points

import math

def main():
    print("This program calculates the distance between two points: ")
    print()

    x1 = float(input("Enter the x coordinate of the first point: "))
    y1 = float(input("Enter the y coordinate of the first point: "))
    x2 = float(input("Enter the x coordinate of the second point: "))
    y2 = float(input("Enter the y coordinate of the second point: "))

    distance = math.sqrt(((x2-x1)**2)+ (y1-y2)**2)

    print("The distance between the two poins is", round(distance,2))
main()