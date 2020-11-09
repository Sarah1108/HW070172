# exercise 4
# function

def sumN(n):
    fact = 1
    for firstsum in range(n,1,-1):
        fact = fact + firstsum
    return fact

def sumNCubes(n):
    factC = 1
    for cube in range(n,1,-1):
        factC = factC + cube**2
    return factC

def main():
    n = int(input("Enter a whole number: "))

    print("The sum of the first natural numbers from", n, "is", sumN(n), "and the Volume is", sumNCubes(n))
main()