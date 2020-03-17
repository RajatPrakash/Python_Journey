# working with function where the arguments requirements can be changed *args


def min_number(*args):
    min = args[0]
    for num in args:
        if num < min:
            min = num
    print(min)


min_number(-8,2,3,4,5,-66,6,7)


# **kwargs (Keyword Arguments)

def user_data(**data):
    for key,value in data.items():
        print(f'{key} = {value}')


user_data(Firstname='Rajat', LastName='Prakash', Contact=8920416458)
