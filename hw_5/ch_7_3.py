# exercise 3, chapter 7

def main():
    # input the exam score
    examS= int(input("Enter your exam score: "))

    # convert exam score to grade with the append method
    
    if examS < 60:
        grade = "F"
    elif 60 <= examS < 70:
        grade = "D"
    elif 70 < examS < 80:
        grade = "C"
    elif 80 < examS < 90:
        grade = "B"
    else :
        grade = "A"
    
    # output resutls in corresponding grade
    print(grade)

main()
