# print name from list and tuple

length = int(input("enter the length of list/tuple: "))
list = []
for i in range(0,length):
    element = input("enter element: ")
    list.append(element)
tuple = tuple(list)
#print(tuple)

#x = ' '.join(tuple)
print(' '.join(tuple))
