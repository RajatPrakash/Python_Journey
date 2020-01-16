import re


def password(value):
    flag = 0
    while True:
        if len(value) < 9:
            print('password length should be atleast 8 character long!')
            flag = 1
            break
        elif re.search('[A-Z]',value) is None:
            print("password should have atleast one character capital")
            flag = 1
            break
        elif re.search('[0-9]',value) is None:
            print("There should be atleast one nnumber to make your password Strong")
            flag = 1
            break
        elif re.search('[!@#$%^&*]',value) is None:
            print("there should be atleast one special character ' ! @ # $ % ^ & * ' ")
            flag = 1
            break
        else:
            flag = 0
            break
    if flag == 0:
        print("correct password")



# user = input("enter the password: ")
# password(user)