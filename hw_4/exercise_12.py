# exercise_12
#   qubes of n natural numbers

def main():
    n = int(input("Enter a whole number: "))
    fact = 1
    for cube in range(n,1,-1):
        fact = fact + cube**2
    print("The sum of the first natural numbers from", n, "is", fact)

main()