import re


def password(user):
    flag = 0
    if len(user) < 8:
        print('Password Length should be greater than or equal to 8')
    elif re.search('[A-Z]', user) is None:
        print('Password should have atleast one Capital Letter')

    elif re.search('[0-9]', user) is None:
        print('Password should have atleast one number ')

    elif re.search('[!@#$%^&*]', user) is None:
        print('Password should have atleast one Special character')
    else:
        print('your password is strong')


user_input = input('Enter Password: ')
password(user_input)
