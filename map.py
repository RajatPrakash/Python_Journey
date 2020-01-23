# the map function takes a list and a function
# the funtion perform an operation on all the elements of list and returns a new list


def add(a, b):
    return a + b


x = [1, 2, 5, 6, 9]
y = [55, 66, 88, 77, 66, 56]

print(x + y)  # this will not add element nut will add both list

c = list(map(add, x, y))
print(c)