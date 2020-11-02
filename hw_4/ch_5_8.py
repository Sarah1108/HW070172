# exercise 8 
#   improved Ceasar cipher
def main(): 
    # get plain text as string from user
    ptext = input("Enter the message you'd like encrypted.\n")
    # get key from user
    key = eval(input("What's the key? : "))

    #format string to lower cases
    ptext = ptext.lower()

    # Create string from list
    ptext = "".join(inputText)

    # Create string of letters
    table= "abcdefghijklmnopqrstuvwxyz"

    # Convert plaintext to ciphertext(cText) using cipher loop
    cText = ""
    for ch in ptext:
        cText = cText + (table[((ord(ch))-97) + key% 52])
    # output the encoded ciphertext
    print("The encoded message is {0}.".format(cText))
main()
