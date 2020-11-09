# chapter 7, exersice 8
# input age and duration of US citizenship
# if 25<= age <30 AND citizenship 7<= citizenship <9 than US representative
# if age => 30 AND citizen ship => 9 than US senator & US representative 
#else print "not eligible to passive right of vote"

def main():
    uscit = int(input("How many years have you been a U.S. Citizen? \n"))
    age = int(input("How old are you? \n"))
    if age >= 30:
        if uscit >= 9:
            print("\nYou are elegeble for the US House of Representatives and the US Senat. ")
    elif 30 > age >= 25: 
        if uscit >= 7:
            print("\nYou are elegeble for the US House of Representatives. ")
    else: 
        print("You are not elegible for neither the US Senat nor the House of Representatives")
main()
