# Fibonnacci sequence

def main():
    print("\nThis Program evaluates the Fibonacci number of a given number.")
    n = int(input("Enter a whole, natural number: "))
    n1= 0
    n2= 1
    sum = n1+n2 
    for i in range(3, n+1):
        sum = sum + n2
    print("\nThe Fibonacci number is: ", sum)
main()