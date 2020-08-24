def main():
    user_input1 = 'y'
    while (user_input1 =='y'):
        is_pali = True
        word = input("enter a potential palindrome: ")
        
        for i in range (len(word)//2):
            if word[i] != word[-(i+1)]:
                is_pali = False
    
        if is_pali == True:
            print("yes")
        else:
            print("no")
        
        user_input1 = input("would you like to try another? ")


main()