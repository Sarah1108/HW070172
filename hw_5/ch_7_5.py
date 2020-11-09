# exersice 5, chapter 7
# 

def main():
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    BMI = (weight*720)// (height**2)
    if BMI < 19: 
        print("Your BMI", BMI,  "is underweight!")
    elif 19 < BMI<= 25:
        print("Your BMI", BMI, "is healthy")
    else:
        print("Your BMI", BMI, "is above the healthy range!")
main()


        