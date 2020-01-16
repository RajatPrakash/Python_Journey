import re

user = input("enter text: ")

# if re.search('[0-9]',user) is None:
#     print("enter atleat one number")
# else:
#     print('correct')

# if re.search('[A-Z]',user) is None:
#     print("atleat one chracter should be capital")
# else:
#     print('correct')

if re.search('[!@#$%^&*]',user) is None:
    print("incorrect")
else:
    print('correct')