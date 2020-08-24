def main():
    user_input = input("Please enter a sentence: ")
    output = ''
    for letter in user_input:
        if (letter=='A' or letter=='a' or letter=='E' or letter=='e' or 
            letter=='I' or letter=='i' or letter=='O' or letter=='o' or 
            letter=='U' or letter=='u'):
            letter = letter.upper()
        else:
            letter = letter.lower()
        output += letter
    print("the output with all consonants in lower case "+
        "and all vowels in upper case will be: " + output)

main()