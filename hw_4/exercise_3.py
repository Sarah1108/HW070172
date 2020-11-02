# exercise 3
#   Molecular weight 

def main():
    print("This programm computes the molecular weight of a carbohydrate.")
    print()
    H = float(input("Hydrogen atoms: "))
    C = float(input("Carbon atoms: "))
    O = float(input("Oxygen atoms: "))
    
    weight = H * 1.00794 + C * 12.0107 + O * 15.99994

    print("The molecular weight is ", weight)

main()