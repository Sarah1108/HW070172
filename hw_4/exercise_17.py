# exercise_17
#   guessing squares roots

import math

def main():
    print("This program help computing square roots.")
    print()
    x = int(input("Enter the number you want to guess the square root of: "))
    n = int(input("Enter the number of times you want to guess: "))
    for guess in range(n):
        guess = int(input("Enter a guess: "))
        guess = guess + (x/guess) / 2
    print("Your guess improved to", guess)
    print("The difference to the actual root is", int(guess- math.sqrt(x)))
main()