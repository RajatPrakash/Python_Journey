import re  #imorting for regular expression

user = input("enter the string")
result = re.search(r'\w\w\w', user)
print(result.group())

result = re.findall(r'w\w\w\w',user)
print(result)