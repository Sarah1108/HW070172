# exercise 2
#   Pizza-price calculation

import math

def main():

    print("This program calculates the cost per square inch of your pizza: ")
    print()

    diameter = float(input("Enter the diameter of your pizza: "))
    price = float(input("Enter the price of your pizza: "))

    pizza = math.pi * (diameter/2) ** 2
    
    print("The price per square inch of your pizza is ", price/pizza)
main()