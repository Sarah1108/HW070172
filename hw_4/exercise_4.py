# exercise 4
#   Lightning strike distance

def main():
    print("This program determines the distance to a lightning strike.")
    print()

    sec = int(input("How many seconds between flash and thunder?: "))

    distance = sec * 1100

    print("The distance to the lightning strike is", distance/5280, "miles.")
main()