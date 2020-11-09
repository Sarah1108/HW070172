# chapter 7 
# exercise 2

def main():
    quizS = int(input("Enter your quiz score: "))

    if quizS == 0:
        grade = "F"
    elif quizS == 1:
        grade = "F"
    elif quizS == 2:
        grade = "D"
    elif quizS == 3:
        grade = "C"
    elif quizS == 4:
        grade = "B"
    else:
        grade = "A"
    # output corresponding grade
    print("The corresponding grade is", grade)
main()