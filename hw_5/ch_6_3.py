#exercise 3
#
import math

def sphereArea(radius): 
    area = 4* math.pi * radius**2
    return area

def sphereVolume(radius):  
    volume = 4/3 * math.pi* radius**3
    return volume

def main():
    print("This programm calculates the Volume and surface area of a sphere.")
    print()

    radius = int(input("Enter the radius of the sphere: "))
    
    print("The Volume of the sphere is", sphereVolume(radius) , "and the surface area is", sphereArea(radius))

main()