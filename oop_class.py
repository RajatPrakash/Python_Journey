# creating a class using OOPs Concept


class Player:
    def __init__(self, name, age):  # __init__ is dunder method
        self.name = name  # attriute or property
        self.age = age
    def property_run(self):
        print('running')


obj = Player('rajat', 23)
obj2 = Player('Cindy', 25)
print('Name:', obj.name, 'Age: ', obj.age)
print('Name:', obj2.name, 'Age: ', obj2.age)
# obj.property_run()
