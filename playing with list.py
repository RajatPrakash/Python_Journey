number = [10, 20, 30, 40]
print(number[:])
number.append(50)  # add number at the lst of the list
new_number = f"new list is {number}"
print(new_number)
number.insert(3, 35)  # insert 35 at index 3
print(number)
number.pop()  # removes the last element
print(number)

# to search a number in list we use index

print(number.index(30))  # it will return the first occurring index of the searched item
print(number.count(10))  # it will return the total count of given number occurring
