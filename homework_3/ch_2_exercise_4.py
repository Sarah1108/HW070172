#chaper 2 programming exercises: 1
#i modified the program by adding a print-statment to the start

def main():

    print("This program converts Celsius temperatures ")
    print("to Fahrenheit.")
    
    for i in range(5):
        celisus = eval(input("What is the Celsius temerature? "))
        fahrenheit = 9/5 * celisus + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit")

    input("Press the <Enter> key to quit.")
main()