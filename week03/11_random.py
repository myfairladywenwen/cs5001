import random as rnd 

num = rnd.random()
print ("random number btw 0.0 and 1.0:", num)

num = rnd.randint(5, 25)
print ("random integer btw 5 and 25:", num)

my_string = "hello world"
print("a random character picked from", my_string+':', rnd.choice(my_string))

print(rnd.choice(["red","green","yellow"]))
