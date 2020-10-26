#exercise 12

def main():
    print("Ths program can caluclate all basic")
    print("mathematical operations. ")
    print("You can use the operators ")
    print("+ for addition, - for subtraction")
    print("* to multiply, / to divide and ** to expone")
    for i in range(100):
        Matex = eval(input("Enter your mathematical expression:    "))
        print(Matex)
    input("Press the <Enter> key to quit.")
main()