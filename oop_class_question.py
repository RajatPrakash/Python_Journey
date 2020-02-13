# 1 Instantiate the Cat object with 3 cats
# 2 Create a function that finds the oldest cat
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj1 = Cat('minks', 2)
obj2 = Cat('ryalie', 3.5)
obj3 = Cat('Mandrine', 5)

print(obj1.name, obj1.age)
print('\n')
print(obj2.name, obj2.age)
print('\n')
print(obj3.name, obj3.age)
print('\n')


def old_cat(*args):
    return max(args)


print(f'Oldest cat is {old_cat(obj1.age, obj2.age, obj3.age)}  year old')
