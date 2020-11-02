#exercise 8
def main():

    print("This program calculates the future value")
    print("of a given time periode investment")
    print("you can both see the yearly as well as the periodic development")

    amYears = eval(input("Enter the number of years for investment:   "))

    principal = eval(input("Enter the intial principal:   "))

    apr, intrate = eval(input("Enter the interest rate divided by a comma:    "))

    initialprincipal = principal

    rate = apr/intrate/100
    print("The interst rate of your investment is: ", rate)

    for i in range(amYears):
        for i in range(intrate):
            principal = principal * (1 + rate)
            print("The value of your investments raised by", principal- initialprincipal, ".")   
    print("The total accumulation of your investments in ", amYears, " years is ", principal , ".")
main()