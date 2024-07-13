
#adding members
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#       self.newAttribute = attr1
#       self.nickName = attr2 

    def printNameAge (self):
        print(self.name, self.age)

    def sayHello(self, message):
        self.message = message
        print(self.message)


petu = Person('gobar', 21)

print(petu.printNameAge())

petu.sayHello('Hello')
