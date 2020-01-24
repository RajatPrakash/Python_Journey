# USING FILTER AND LAMBDA EXPRESSION, WRITE A CODE THAT TAKES
# A LIST OF NUMBERS BELOW AND RETURNS EVEN NUMBERS ONLY

upper_limit = int(input('Upper limit: '))
lower_limit = int(input('Lower Limit: '))

my_list = list(range(upper_limit, lower_limit))

output = list(filter(lambda x: (x% 2 == 0),my_list))

print(output)