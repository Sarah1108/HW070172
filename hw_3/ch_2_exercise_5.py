#chaper 2 programming exercises: 1
#i modified the program by adding a print-statment to the start

def main():

    print("This program prints alls Celsius temperatures from 0-100 degrees")
    print("to their Fahrenheit equivalent in 10 degree Celsius steps.")
    
    for c in [0,10,20,30,40,50,60,70,80,90,100]:
        fahrenheit = 9/5 * c + 32
        print(c, " degrees Celsius is ", fahrenheit, "degrees Fahrenheit")

    input("Press the <Enter> key to quit.")
main()