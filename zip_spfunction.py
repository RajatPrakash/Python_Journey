# using the zip function to add to iterables can be list / tuples and anything


user_name = ['Cas', 'Marry', 'Dean', 'Sam']
age = [2100, 42, 31, 29]
case = ('angel', 'Mother', 'alpha', 'geek')
extra = [2, 4]

print(list(zip(user_name, age)))
# output -- [('Cas', 2100), ('Marry', 42), ('Dean', 31), ('Sam', 29)]

print(list(zip(user_name, age, case)))
# output -- [('Cas', 2100, 'angel'), ('Marry', 42, 'Mother'), ('Dean', 31, 'alpha'), ('Sam', 29, 'geek')]

print(list(zip(user_name, age, case, extra)))
# output -- [('Cas', 2100, 'angel', 2), ('Marry', 42, 'Mother', 4)]

# extra list has only 2 items so list created but containing on 2 tuples , dean and sam were removed
