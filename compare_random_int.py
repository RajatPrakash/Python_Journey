# QUESTION: write a code that take number from user and compare it to
# a random genrated number and states which oneis LARGER / SMALLER

import random

user_input = int(input('Enter a number: '))
random_input = random.randint(0, 1000)
if user_input < random_input:
    print('Your Number is Smaller than Computer Generated number')
elif user_input > random_input:
    print('Your Number is Larger than Computer Generated number')
else:
    print("WOW.. That's a tie")