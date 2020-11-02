# exercise 5
#   Konditorei coffe 

def main():
    print("This program calculater the cost of a coffee order at Cafe Konditorei.")
    print()

    pounds = float(input("How many pounds do you want to order:  " ))

    totalcost = pounds * 10.5 + pounds * 0.86 + 1.50

    print("The cost of your coffee order is", round(totalcost,2))
main()