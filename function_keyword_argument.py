# working with function key word argument

sum = 0


def add(num1, num2):
    sum = (num1**2) + (num2**2)
    #print(sum)
    return sum


# taking input from user
number1 = float(input('Enter the first number '))
number2 = float(input('Enter the second Number'))

print(add(num1=number2, num2=number1))  # Passing the keyword Argument

