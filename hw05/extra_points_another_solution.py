PUMP_ON_WATTS = 500
# take 500 as the point that marks the using of well to pump water
# the number comes from the average of
# the amount when it is pumping(1000) and when it is off(0)
PERIOD = 120


def main():
    ''' read the file recording the pump working data and
    analyze the water producing and electricity consuming process,
    with particular attention to the duration of 120 min to
    analyze the behavior of the water softener.
    None -> None'''
    try:
        filename = input('Please enter the file name: ')
        yourfile = open(filename, 'r')
    except:
        print("Can't open that file.")
        return
    minutes = 0
    record_lst = []  # initiate an empty list to record those pumping water
    print('Information on water softener recharges:')
    for line in yourfile:
        minutes += 1
        line_in_min = int(line)
        if line_in_min >= PUMP_ON_WATTS:
            record_lst.append(line_in_min)
        else:
            if len(record_lst) >= PERIOD:
                print(str(len(record_lst)) + ' minute run started at' +
                      str(minutes - len(record_lst)))
            record_lst = []


main()
