# exercie_14
#       creating an average of a chosen amount of numbers

def main():
    print("This program is caluculating the average of a choosen amount of numers.")
    print()
    amountOfNumers= int(input("How many numbers do you want to add: "))
    print()
    for fact in range(amountOfNumers,0,1):
        fact = fact + int(input("Add the number: "))# still don't know how to do this step, see exercise 13
    print("The average of numbers is", float(fact/amountOfNumers))
main()

    
