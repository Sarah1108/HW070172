# exercise 1 
#   This programm calculates the Volume and sufacse area of a sphere.

import math

def main():
    print("This programm calculates the Volume and surface area of a sphere.")
    print()

    radius = int(input("Enter the radius of the sphere: "))

    Volume = 4/3 * math.pi* radius**3
    area = 4* math.pi * radius**2
    print("The Volume of the sphere is", Volume, "and the surface area is", area)

main()