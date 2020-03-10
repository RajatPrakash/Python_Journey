#  using map function in python

my_list = [1, 2, 3, 4]


#  Creating a normal function
def mul(list):
    new = []
    for i in list:
        new.append(i ** 2)

    return new


print(mul(my_list))


# Doing same thing with map function

def square(list2):
    return list2 ** 2


print(list(map(square, my_list)))


#  Optimising the above code with the help of anonymous function Lambda
print(list(map(lambda x: x**2, my_list)))
