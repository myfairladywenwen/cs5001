import random as rnd 
key = rnd.randint(0,100)

counter = 0
guess = int(input("guess a num btw 0 and 100: "))
counter+=1
while guess!= key:
    if guess > key:
        guess = int(input("your answer is bigger, try again: "))
    else:
        guess = int(input("your answer is smaller, try again: "))
    counter+=1
print("correct, you get the key in", counter, "tries.")