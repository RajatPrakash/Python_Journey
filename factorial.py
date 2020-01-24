# FUNCTION THAT TAKES A VARIABLE AND RETURNS ITS FACTORIAL
"""
    fact  = fact *value - 1


"""


def factorial(value):
    fact = 1
    while value > 0:
        fact = fact * value
        #print(fact)
        value = value-1

    print(fact)


user_input = int(input('Enter the number: '))
factorial(user_input)