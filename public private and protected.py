# making varibale states as public / private/ protected

class Test:
    def __init__(self):
        self.pub = 'I am Public variable'
        self._pro = 'I am Protected Variable'
        self.__pri = 'I am the Private One'

    def puby(self):
        print(" I am the public method , easily accessible")

    def _proy(self):
        print(" I am the Protected method , not so easily accessible")

    def __priy(self):
        print(" I am the PRIVATE method , only single spell can make me accessible")

#testing
entity = Test()

# lets access the variables
print(entity.pub)
print(entity._pro)
# accessing the private variable
print(entity._Test__pri)

# lets access the methods
entity.puby()
entity._proy()

# accessing the private method
entity._Test__priy()
