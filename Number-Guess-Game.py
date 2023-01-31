import random
print("Number Guessing Game")
rand=random.randint(1,10)
flag = 0
while flag < 1 :
    guess=int(input("Guess a number between 1 & 10 : "))
    if rand == guess:
        print("You have won!")
        flag = 1
    else:
        print("Try again")
