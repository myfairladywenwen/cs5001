def main():
    #define each bound as constants
    LOWER_BOUND_Z1, UPPER_BOUND_Z1, UPPER_BOUND_Z2, UPPER_BOUND_Z3, UPPER_BOUND_Z4, UPPER_BOUND_Z5\
        = 0.50, 0.60, 0.70, 0.80, 0.90, 1.00
    #The lowest value for a given zone should be 
    #0.01 greater than the highest value for the previous zone
    EDGE = 0.01
    #prompt for user input of his age and resting heart rate
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    print("=======================================")

    #TODO: Fill in the rest of the necessary code here

    print("=======================================")

    #max heart rate = 208 - 0.7 * age
    max_hr = 208 - 0.7 * age

    #heart rate reserve = max heart rate - resting heart rate
    hr_reserve = max_hr - restHR

    # calculate each heart rate zone
    hr_zone1_lower_bound = round(restHR + hr_reserve * LOWER_BOUND_Z1, 2)
    hr_zone1_upper_bound = round(restHR + hr_reserve * UPPER_BOUND_Z1, 2)
    hr_zone2_lower_bound = round(hr_zone1_upper_bound + EDGE, 2)
    hr_zone2_upper_bound = round(restHR + hr_reserve * UPPER_BOUND_Z2, 2)
    hr_zone3_lower_bound = round(hr_zone2_upper_bound + EDGE, 2)
    hr_zone3_upper_bound = round(restHR + hr_reserve * UPPER_BOUND_Z3, 2)
    hr_zone4_lower_bound = round(hr_zone3_upper_bound + EDGE, 2)
    hr_zone4_upper_bound = round(restHR + hr_reserve * UPPER_BOUND_Z4, 2)
    hr_zone5_lower_bound = round(hr_zone4_upper_bound + EDGE, 2)
    hr_zone5_upper_bound = round(restHR + hr_reserve * UPPER_BOUND_Z5, 2)
    # print them
    print('Your heart rate reserve is:', hr_reserve, 'bpm')
    print('Here is a breakdown of your training zones:')
    print('Zone 1:', hr_zone1_lower_bound, 'to', hr_zone1_upper_bound, 'bpm')
    print('Zone 2:', hr_zone2_lower_bound, 'to', hr_zone2_upper_bound, 'bpm')
    print('Zone 3:', hr_zone3_lower_bound, 'to', hr_zone3_upper_bound, 'bpm')
    print('Zone 4:', hr_zone4_lower_bound, 'to', hr_zone4_upper_bound, 'bpm')
    print('Zone 5:', hr_zone5_lower_bound, 'to', hr_zone5_upper_bound, 'bpm')
main()
