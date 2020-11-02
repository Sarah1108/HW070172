#exercise 9
#   geometrie, triangle

import math

def main():
    print("This program calculates the area of a triangle.")
    print()

    a = float(input("Enter the length of a: "))
    b = float(input("Enter the length of b: "))
    c = float(input("Enter the length of c: "))

    s = (a+b+c)/2

    area = math.sqrt(s*(s - a)*(s - b)*(s - c))

    print("The area of a this triangle is", area)

main()