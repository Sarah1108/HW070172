# exercise 6

def main():
    speedlim = int(input("Enter the speed limit: "))
    actualspeed = int(input("Enter the speed: "))
    if actualspeed < speedlim:
        print("Your speed is legal.")
    elif speedlim < actualspeed < 90 :
        fees= 50+ ((actualspeed-speedlim)*5)
        print("Your speed is illeagal and your fees: ", fees)
    elif actualspeed > 90:
        fees= 250+((actualspeed-speedlim)*5)
        print("Your speed is illeagal and your fees: ", fees)
main()
