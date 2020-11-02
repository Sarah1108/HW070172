#convert.py
#   A program to convert Celisus temos to Fahrenheit.
# By Susan Computewell (Phyton Book p.30)

def main():
    fahrenheit = eval(input("What is the Fahrenheit temerature? "))
    celsius = (fahrenheit-32)/ (9/5)
    print("The temperature is", celsius, "degrees Celsius")
main()