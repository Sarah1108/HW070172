# exercise_16
# Fibonacci sequence

def main():
    print("This Program calculates two chosen numbers of the Fibonacci sequence")
    print()
    n = int(input("Enter a whole natural number:  "))
    n1 = 1
    n2 = 1
    for n1,n2 in range(3, n+1):
        n1, n2 = n2, n1 + n2
    print("The number is", n2)
main()