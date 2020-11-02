# exercise 5
#   Numeric value of a name

def main():
    # get input name
    name = input("Enter your name: \n")

    #convert all letters to lower
    name = name.lower()

    #convert to numbers, subtract 96 from each Unicode Standard
    x = 0
    for ch in name:
        x = int(ord(ch)) + x - 96
    # accumulate and output
    print("The numeric value of your name is {0}.".format(x))
main()

