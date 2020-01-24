#  WRITE A CODE THAT TAKES A RANGE FROM A USER (UPPER AND LOWER BOUND)
#  AND RETURNS A LIST OF POSITIVE AND EVEN NUMBERS ONLY

upper = int(input('enter the upper limit: '))

lower = int(input('enter the lower limit: '))

my_list = list(range(upper, lower))

result = list(filter(lambda x: (x>0 and x%2 == 0), my_list))

print(result)