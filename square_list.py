# SCRIPT WHOSE ITEMS ARE SQUARES OF THE ORIGINAL LIST

my_list = list(range(1, 10))

# print(my_list)

square_list = list(map(lambda x: x ** 2, my_list))
print(my_list)
print(square_list)

