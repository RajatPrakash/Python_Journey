# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print
# the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names
# alphabetically and print each name on a new line.
import numbers

number = int(input('Enter the number of students whose records you want to store:'))

my_list = []

# Creating nested list which is taking input from the user
for i in range(number):
    my_list.append([])
    for j in range(1):
        name = input('Name:')
        marks = int(input('Marks:'))  # physics marks only
        my_list[i].append(name)
        my_list[i].append(marks)

# print(my_list)


def getname(lsit):
    test = []
    for i in my_list:
        for j in i:
            if isinstance(j, int):
                test.append(j)

    test.sort()
    second_last = test[-2]
    for i in my_list:
        if second_last == i[0] or second_last ==i[1]:
            print(i[0])


getname(my_list)
#  c = [y for x,y in my_list if isinstance(x, int)]
#  c = list(filter(lambda x[1]: isinstance(x[1], int), my_list))
# print(clear(my_list))

# nested list
# new_list=[]
# for i in range(5):
#     new_list.append([])
#     for j in range(5):
#         new_list[i].append(j)
#
#
# print(new_list)
