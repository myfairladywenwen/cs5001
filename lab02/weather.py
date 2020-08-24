temp_high1, temp_low1, temp_noon1 = 73, 58, 66
temp_high2, temp_low2, temp_noon2 = 77, 60, 69
temp_high3, temp_low3, temp_noon3 = 71, 60, 66
temp_high4, temp_low4, temp_noon4 = 67, 57, 64
temp_high5, temp_low5, temp_noon5 = 62, 53, 60
temp_high6, temp_low6, temp_noon6 = 65, 54, 60
temp_high7, temp_low7, temp_noon7 = 63, 55, 59
temp_high8, temp_low8, temp_noon8 = 65, 55, 60
temp_high9, temp_low9, temp_noon9 = 67, 55, 62
temp_high10, temp_low10, temp_noon10 = 69, 56, 63
#question1:diff between highest and lowest
diff = temp_high1 - temp_low5
print("the difference between the highest and the lowest temperature values " + 
"predicted for the 10 day forecast is", diff, end='')
print("F")

#question2:average for noon
avg_noon =(temp_noon1 + temp_noon2 + temp_noon3 + \
     temp_noon4 + temp_noon5 + temp_noon6 + temp_noon7 + \
         temp_noon8 + temp_noon9 + temp_noon10)/10
print("the average temperature at noon predicted for the 10 day forecast is", avg_noon, end='')
print("F")

#question3:highest temperature predicted for the 10 day, converted from F to C
highest_temp_c = (temp_high1 - 32) * 5/9
print("the highest temperature predicted for the 10 day is", highest_temp_c, end='')
print("C")
