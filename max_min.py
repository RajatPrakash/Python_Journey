#python class to find out max and min between two number

class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def max(self):
        if self.a > self.b:
            print(f"max of two number {self.a} and {self.b} is {self.a}")
        else:
            print(f"max of two number {self.a} and {self.b} is {self.b}")

    def min(self):
        if self.a < self.b:
            print(f"min of two number {self.a} and {self.b} is {self.a}")
        else:
            print(f"min of two number {self.a} and {self.b} is {self.b}")


num1 = int(input("enter the first number: "))
num2  = int(input("enter the second number: "))

object = Number(num1, num2)
object.max()
object.min()