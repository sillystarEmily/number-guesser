# this code is to generate a randome number that the user has to guess for

# random number import
import random

#prints/makes the random number
number_random = random.randint (1,100)
print("Random number generated")

#code for the guessing of the number, what you see when printed 

guessed_number = int(input("Guess a number that is between 1-100: "))

while guessed_number!=number_random:
    if guessed_number<number_random:
        guessed_number = int(input("Guess higher: "))
    else:
        guessed_number = int(input("Guess lower: "))

#taken out of the while loop so it can work without interfering with the loop

guessed_number = int(input("You got the right number!!"))




