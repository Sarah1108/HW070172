#exercise 10 
#   average word lenght

def main():
    # get input
    text = input("Enter your sentence: \n")

    #initialize output list
    numWords = []

    #loop for duration of input list split
    for string in text.split():
        #create a temporary variable to store the
        #first letter of each word
        x = string[0]
        numWords.append(x)
    
    letTotal = 0
    for string in text.split():
        letTotal = len(string) + letTotal
        wAvg = letTotal / (len(numWords))

    #put togehter listed out put and print
    print(wAvg)

main()