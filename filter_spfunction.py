# using the filter function to receive particualr output without affecting the original list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def check_even(items):
    return items % 2 == 0


def check_odd(items):
    return items % 2 != 0


print(list(filter(check_even, my_list)))
print(list(filter(check_odd, my_list)))

# just to check the main difference between the map and filter function
print(list(map(check_even, my_list)))  # understood


# Optimal way Use of lambda function the anonymous king
# for even
print(list(filter(lambda x: x % 2 == 0, my_list)))

# for odd
print(list(filter(lambda x: x % 2 != 0, my_list)))