# WRITE A FUNCTION THAT SQUARES A VARIABLE AND THEN TEST THE FUNCTION USING A LIST OF INTEGER NUMBERS RANGING FROM
# -20 to 20


def square(x):
    return x**2


my_list = list(range(-20, 20))

result = list(map(square, my_list))

print(result)

