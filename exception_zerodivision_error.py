try:
    a,b = [int(x) for x in input("enter two number").split()]
    print(a,b)
except ValueError:
    print("More than two values are not allowed!")

print(a+b)