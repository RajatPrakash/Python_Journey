
# to check the target sum of three in a array exists or not
class Solution(object):
    def __init__(self, list, target):
        self.list = list
        self.target = target

    def calculation(self):
        i = 0
        j = len(list) - 1
        while (True):
            if i < j:
                if list[i] + list[j] == target:
                    print(list[i], list[j])
                i = i + 1
            elif i == len(list) - 1:
                j = j - 1
                i = 0
            elif j == 0:
                break


length = int(input("enter the length of the list: "))
target = int(input("Enter the target: "))
list = []
for i in range(0, length):
    element = int(input("element: "))
    list.append(element)

object = Solution(list, target)
object.calculation()

