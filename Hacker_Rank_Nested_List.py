# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print
# the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names
# alphabetically and print each name on a new line.
#
# number = int(input('Enter the number of students whose records you want to store:'))
#
# items = 2  # name and marks of student
#
# my_list = []
#
# for i in range(0,number):
#     while items < 2:
#         name = input('Name:')
#         marks = float(input('Marks:'))  # physics marks only
#         my_list.append(name,marks)
#         #my_list.append(marks)
#         j+=1
#
# print(my_list)
new_list=[]
for i in range(5):
    new_list.append([])
    for j in range(5):
        new_list[i].append(j)


print(new_list)