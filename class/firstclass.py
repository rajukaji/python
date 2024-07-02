#class: blueprint for creating new objects
#object: is the instance of class

#class:Human
#objects: John, Ramu, gobarePetu
#class has methods

#creating class

class ClassName:
    def func(self):
        print("self")

function = ClassName()
print(type(function))

print(isinstance(function, ClassName))#true or false value function is instance of ClassName
