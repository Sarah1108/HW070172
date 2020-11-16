# exercise 6 
import math as m

def primenum():

    x = m.sqrt(n)
    i = 2
    while i <= x:
        value = n % i
        #if any value is divisble, break and close program
        if value == 0:
            return
        #if no value is divisible evenly, print("The number is prime.")
        else:
            i = i + 1
    print(n)
#Validate n as a positive whole number
def main():
    n = 0

    while True:
        n = eval(input("Input a positive whole number: "))

        if (n % 1 != 0):
            n = print("The number you entered was not whole!")
        elif (n < 1):
            n = print("The number you entered was not positive!")
        else:
            break
    # it says that it takes = postional argument, but I don't understand the error
    for i in range(n):
        primenum(n+1)

    print("The number is prime.")

main()