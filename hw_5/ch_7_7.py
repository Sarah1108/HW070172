#exercise 7 chapter 7
# babysitter


def main():
    # input date time start
    # input date time end
    sttime = input("Enter the start time: ")
    etime = input("Enter the end time: ")   
    # turn the strings into numbers
    sthour = eval(sttime[-2:len(sttime)])
    stmin = eval(sttime[:len(sttime)-3])
    ehour = eval(etime[-2:len(etime)])
    emin = eval(etime[:len(etime)-3])
    # turn the numbers into time
    sttime = sthour + 1 /(60/stmin)
    etime = ehour + 1/(60/emin)
    # calculate the time span
    time = etime - sttime
    # if the whole time before 9p.m. * 2.50
    if etime < 21:
        costs = time * 2.50
    # if the time is after 9p.m. 
    #   calulate time before 9 * 2.50
    #   caculate time after 9 * 1.75
    #   add the times
    else: 
        x = etime -21
        costs = (time -x) * 2.50 + (x * 1.75)
    # print output in a rounded proper layout
    print("The babysitting costs ${0}".format(round(costs, 2)))
main()