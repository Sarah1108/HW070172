#interest rate, loop that tell you when the investment is double the size 

def main():
    apr = eval(input("What is the annualized interest rate? "))
    apr = .01*apr
    principal = eval(input("What is the initial principal? "))

    p = principal
    interest = 0
    years = 0
    
    while principal > .5 * p:
        years = years + 1
        interest = p * apr
        p = p + interest

    print("The amount of", p)
    print("will be reached in", years)

main()