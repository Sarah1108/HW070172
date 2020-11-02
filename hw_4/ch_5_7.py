# exercise 7 
#   Ceasar cipher

def main(): 
    # get plain text as string from user
    ptext = input("Enter the message you'd like encrypted.\n")
    # get key from user
    key = eval(input("What's the key? : "))

    # Create string from list
    ptext = "".join(inputText)

    # Convert plaintext to ciphertext(cText) using cipher loop
    cText = ""
    for ch in ptext:
        cText = cText + (ch(ord(ch) + key))
    # output the encoded ciphertext
    print("The encoded message is {0}.".format(cText))
main()
