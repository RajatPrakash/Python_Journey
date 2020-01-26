# reading data from a file

data = open('Python_codes_list.txt', 'r')
print(data.read())  # .read() will read the whole file

print(data.readline())  # this will read only the first line of the text file
