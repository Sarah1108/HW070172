# exercise 9
#   word count

def main(): 
    # get input sentence
    text = input("Write your sentence: \n")

    # initialize output list
    word_len = []

    # loop for duration of input split
    for string in text.split(): 
        # create a temporary variable to store the first
        # letter of the word 
        x = string[0]
        word_len.append(x)

    #put together listed output strings and print
    print(len(word_len))

main()

