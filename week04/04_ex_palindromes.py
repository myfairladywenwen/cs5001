def main():
    user_input1 = 'y'
    while (user_input1 =='y'):
        user_input1 = input("enter a potential palindrome: ")
        user_input2 = ''
        for i in range (len(user_input1)-1, -1, -1):
            user_input2 += user_input1[i]
    
        if user_input1 == user_input2:
            print("yes")
        else:
            print("no")
        user_input1 = input("would you like to try another? ")


main()