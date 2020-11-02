# exercise 2
#   Grade scale

def main():
    # input quiz score from user
    quizS = int(input("Enter your quiz score: "))

    # convert the quiz score to grades
    grades = ["F", "F", "D", "C", "B", "A"]
    quizS = grades[int(quizS)]

    # output corresponding grade
    print("The corresponding grade is {} .".format(quizS))
main()