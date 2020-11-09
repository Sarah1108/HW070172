# chaper 7 exercise 1
def main(): 
    workhours = int(input("How many hours did you wirk this week? "))
    wagephour = float(input("How much do you earn per hour? "))
    if workhours <= 40:
            wage= workhours * wagephour
    else:
            wage = (40* wagephour) + (workhours-40)* 1,5* wagephour
    print("The wage is", wage)    
main()