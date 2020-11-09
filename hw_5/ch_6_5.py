# exercise 5, chaper 6
# pzza convert 

import math

def pizzaAr(diameter):
    pizza = math.pi * (diameter/2) ** 2
    return pizza

def pizzaprice(price, pizza):
    pricepsq = price / pizza
    return pricepsq

def main():
    print("This program calculates the cost per square inch of your pizza: ")
    print()
    diameter = float(input("Enter the diameter of your pizza: "))
    price = float(input("Enter the price of your pizza: "))
    pizza = pizzaAr(diameter)
    pricepsq = pizzaprice(price, pizza)
    print("The price per square inch of your pizza is ", pricepsq)
main()

