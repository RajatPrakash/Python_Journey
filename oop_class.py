# creating a class using OOPs Concept


class Player:
    # class object attribute
    membership = True  # it is static attribute its value will always remains the same

    def __init__(self, name, age):  # __init__ is dunder method
        self.name = name  # attriute or property
        self.age = age
    def property_run(self):
        print('running')


# taking user input for dynamic calling of the class

while True:
    player_name = input('Enter player Name? ')
    player_age = int(input('Enter player age? '))
    obj = Player(player_name, player_age)
    print('Name:', obj.name, 'Age: ', obj.age)

    user_continue = input('Do you want to print more players name? yes or no?')
    if user_continue == 'no':
        break
    else:
        continue
