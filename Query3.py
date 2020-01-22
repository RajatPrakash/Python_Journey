# Question: write a script that will prompt a user for an input and
# checks if the number is divisible by 5 but not  a multiple of 7


def cal():
    user_input = int(input('Enter a number! '))
    if user_input % 5 == 0 and user_input % 7 != 0:
        print('Number is accepted by the code')
    else:
        print("nah that's not your number, Try again please")
        cal()


cal()
