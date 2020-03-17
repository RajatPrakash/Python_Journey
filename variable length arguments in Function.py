# working with function where the arguments requirements can be changed


def min_number(*args):
    min = args[0]
    for num in args:
        if num < min:
            min = num
    print(min)


min_number(-8,2,3,4,5,-66,6,7)
