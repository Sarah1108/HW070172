# exercise 10
#   length of a ladder

import math

def main():
    print("This program calculates the needed lenght of a ladder.")
    print()

    height = float(input("Height of the object: "))
    angle = float(input("Enter the angle the ladder should lean: "))

    lenght = height/ math.sin(angle)

    print("The needed lenght to reach the object is: ", lenght)

main()