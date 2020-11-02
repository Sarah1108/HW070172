#exercise 6
#   modifying exersice 5 to take more names as input

def main():
    # get input name
    name = input("Enter your name: \n")

    #convert all letters to lower, account for user input
    fName = "".join(name)
    fName = fName.lower()
    fName = fName.lstrip()
    fName = fName.replace(" ", " ")
    fName = fName.replace("-", " ")

    #convert to numbers, subtract 96 from each Unicode Standard
    x = 0
    for ch in name:
        x = int(ord(ch)) + x - 96
    # accumulate and output
    print("The numeric value of your name is {0}.".format(x))
main()