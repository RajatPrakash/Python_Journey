# creating a class using OOPs Concept


class Player:
    def __init__(self, name):
        self.name = name

    def property_run(self):
        print('running')


obj = Player('rajat')
print(obj.name)
obj.property_run()
