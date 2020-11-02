#exercise 3 
#   exam scores

def main():
    # input the exam score
    examS= int(input("Enter your exam score: "))

    # convert exam score to grade with the append method
    grade=[]
    for x in range(0,60):
        grade.append("F")
    for x in range(60,70):
        grade.append("D")
    for x in range(70,80):
        grade.append("C")
    for x in range(80,90):
        grade.append("B")
    for x in range(90,100):
        grade.append("A")
    
    # output resutls in corresponding grade
    print(grade[examS])

main()

    