# using for loop to read text file data

data = open('new_file.txt', 'r')

for i in data:
    word = i.split()
    print(word)  # printing data word wise

for i in data:
    print(i)  # printing data line wise
