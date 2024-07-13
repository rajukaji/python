class Name:
    def __init__(self, name):
        self.name = name

        
    def callMyName(self, passObject):
        print(self.name)
        print(passObject.name)


#creating object
person1 = Name('Petu')
person2 = Name('Mottu')

person1.callMyName(person2)
print(person1.name)

person2.callMyName(person1)
