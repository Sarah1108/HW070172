# exercise_11
#   sum of n natural numbers

def main():
    n = int(input("Enter a whole number: "))
    fact = 1
    for firstsum in range(n,1,-1):
        fact = fact + firstsum
    print("The sum of the first natural numbers from", n, "is", fact)

main()