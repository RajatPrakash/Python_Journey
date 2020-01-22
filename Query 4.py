# Question: write a code that takes an input from the user and indicates its number of digits

user_input = int(input('Enter your number: '))

# there are may ways to solve this problem
# first way converting it into string and then using a flag

#  user_input = str(user_input)

# count = 0
# for i in user_input:
#     count += 1
# print(count)
#
# # second way using length funtion on string
#
# print(len(user_input))

# third way
flag = 0
while user_input > 0:
    if user_input > 0:
        user_input = int(user_input / 10)
        flag +=1
print('Number of digits in your input', flag)
