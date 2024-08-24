import random
import math
#Taking Inputs
lower = int(input("Enter Lower Bound:- "))
upper = int(input("Enter Upper Bound:- "))
#Generating random number between the lower and the upper
x = random.randint(lower,upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tYou've only ", total_chances, " chances to guess the integer!\n")

#Initializing the number of guesses
count = 0 
flag = False
#for caluulation of minimum number of guesses depending on range
while count < total_chances:
    count += 1
    #taking guesses as the input number
    guess = int(input("Guess a number:- "))
    #condition testing
    if x == guess:
        print("Congratulations you did it in ", count, " try")
        #once guessed, break the loop
        flag = True
        break
    elif x > guess:
        print("You guessed to small!")
    elif x< guess:
        print("You guessed too high!")

#if guessing is more than required guesses, shows this output
if not flag:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next Time!")