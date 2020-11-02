# exercise_15
#   A program to approximate the value of pi

import math

def main():
    print("This program aproximates the value of pi.")
    print()
    n = int(input("Enter the number of terms to sum: "))
    total = 0 
    for i in range(n):
        total = total + 4*(-1)** i /(2*i+1)
    print("The aproximate value of pi is", total, ".")
    print("The difference to actual pi is", math.pi - total)
main()