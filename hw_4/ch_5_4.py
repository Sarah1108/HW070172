# exercise 4
#   Acronym program
def main():
    #get input from user
    oldname = input("What would you like to turn into an acronym? \n")

    #start output list
    words = []

    #loop 
    for string in oldname.split():
        # have an additional variable to store the first letter
        # in upper case
        x = string[0].upper()
        words.append(x)
    #put together listed output strings and print
    acronym = "".join(words)

    print(acro)
main()