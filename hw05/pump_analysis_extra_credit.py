import math
MIN_PER_HOUR = 60
HOUR_PER_DAY = 24
GALLON_PER_MIN = 2
WATT_PER_KWT = 1000
GALLON_VOL1 = 5
GALLON_VOL2 = 100
USER_GALLEN_1 = 5
USER_GALLEN_2 = 100
# set -1 as the default output for the amount of gallons that
# can not be reached during the time period.
MISSION_IMPO = -1
# take 500 as the point that marks the using of well to pump water
# the number comes from the average of
# the amount when it is pumping(1000) and when it is off(0)
PUMP_ON_WATTS = 500
PERIOD = 120


def main():
    ''' read the file recording the pump working data and analyze
    the water producing and electricity consuming process,
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
    pump_minutes = 0
    watt_sum = 0

    result1_done = False
    result2_done = False

    time_lst = []  # initiate an empty list to record the minutes pumping water

    for line in yourfile:
        line_in_min = int(line)
        minutes += 1
        if line_in_min >= PUMP_ON_WATTS:
            time_lst.append(minutes)
            pump_minutes += 1
        if (pump_minutes >= math.ceil(USER_GALLEN_1 / GALLON_PER_MIN) and
                not result1_done):
                    time_gallon1 = minutes
                    result1_done = True
        if (pump_minutes >= math.ceil(USER_GALLEN_2 / GALLON_PER_MIN) and
                not result2_done):
                    time_gallon2 = minutes
                    result2_done = True
        watt_sum += line_in_min

    hour = minutes / MIN_PER_HOUR
    day = hour / HOUR_PER_DAY

    sum_gallon = GALLON_PER_MIN * pump_minutes
    gallaon_per_day = sum_gallon * HOUR_PER_DAY / hour

    print('Data covers a total of', hour, 'hours')
    print('(That\'s', day, 'days)')
    print()
    print('Pump was running for ' + str(pump_minutes) +
          ' minutes, producing ' + str(sum_gallon) + ' gallons')
    print('That\'s', gallaon_per_day, 'gallons per day')
    print()

    watt_sum_in_kwh = round(watt_sum / WATT_PER_KWT / MIN_PER_HOUR, 5)
    print('Pump required a total of', watt_sum, 'watt minutes of power')
    print('That\'s', watt_sum_in_kwh, 'kWh')
    print()

    if result1_done:
        print('It took ' + str(time_gallon1) + ' minutes of data to reach ' +
              str(USER_GALLEN_1) + ' gallons.')
    if result2_done:
        print('It took ' + str(time_gallon2) + ' minutes of data to reach ' +
              str(USER_GALLEN_2) + ' gallons.')
    else:
        print('It took ' + str(MISSION_IMPO) + ' minutes of data to reach ' +
              str(USER_GALLEN_2) + ' gallons.')
    print()

    print('Information on water softener recharges:')
    start = 0
    while start < len(time_lst):
        for end in range(start + 1, len(time_lst)):
            duration = end - start
            if (time_lst[end] - time_lst[end - 1] > 1):
                if duration >= PERIOD:
                    print(str(duration) + ' minute run started at ' +
                          str(time_lst[start]))
                start = end


main()
