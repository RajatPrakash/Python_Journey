list =[1, 2, 3, 4, 5, 6, 8, 2, 3, 4, 5, ]
unique=[]
for number in list:
    if number not in unique:
        unique.append(number)
        unique.sort()
print(unique)