# exercise 4 
# chapter 4

def main():
    credits = int(input("How many credits have you earned? "))

    if credits < 7:
        grade = "Freshman"
    elif 7 < credits < 16:
        grade = "Sophomore"
    elif 16 <=  credits < 26:
        grade = "Junior"
    else :
        grade = "Senior"
    print(grade)
main()