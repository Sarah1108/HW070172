def main():

    #print an introduction(print statement)

    print("This program calculates the future value")
    print("of a given time periode investment")

    amYears = eval(input("Enter the number of years for investment:   "))

    principal = eval(input("Enter the annual principal:   "))

    apr = eval(input("Enter the annual interest rate:   "))

    for i in range(amYears):
        principal = principal + principal * (1 + apr)

    print("The total accumulation of your investments in ", amYears, " years is ", principal, ".")    
main()