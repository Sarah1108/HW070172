def main():

    #print an introduction(print statement)

    print("This program calculates the future value")
    print("of a given time periode investment")

    amYears = eval(input("Enter the number of years for investment:   "))

    principal = eval(input("Enter the annual principal:   "))

    apr = eval(input("Enter the annual interest rate:   "))

    intialprincipal = principal

    rate = apr + 1

        for i in range(amYears):
            principal = intialprincipal + principal * rate
            print("The total accumulation of your investments in ", amYears, " years is ", principal, ".")    
main()