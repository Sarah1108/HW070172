# exercise_13
#   sum by wish, loops and inputs
# I couldn't solve this! 
def main():
    print("This programm calculates the sum of a wished series of numbers.")
    print()
    amountOfNumbers = int(input("How many numbers shall be summed up: "))
    totalsum = 0
    for add in range(1,amountOfNumbers+1): #not sure how to construct the formula
        add = int(input("Enter the number you wish to add: "))
        totalsum = add + totalsum
    print("The sum of the entered numbers is", totalsum)
main()