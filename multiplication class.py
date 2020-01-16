# create a class to find multiplication of any number

class Multiplication:
    def __init__(self,num):
        self.num = num

    def table(self):
        for i in range(1,10+1):
            print(f"{self.num} * {i} = {self.num * i}")       #  5 * 1 = 5


object = Multiplication(int(input("enter the number who's table you want to find out: ")))
object.table()
