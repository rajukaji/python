class Animal:
    def __init__(self):
        self.age = 1


    def eat(self):
        print("Eat")

class Mammal(Animal):#animal is a parent or base class
    # def eat(self):
    #     print("Eat")


    def walk(self):
        print("Walk")


class Fish(Animal):#animal is a base class
    # def eat(self):
    #     print("Eat")

    def swim(self):
        print("swim")


#Animal is a base or parent class
#Mammal: adn Fish are child or sub class
m = Mammal()#create mammal object
m.eat()
print(m.age)

print(isinstance(m, Mammal)) #is m an instance of Mammal?

#object is the base class for all the clases in python. 
#even for the parent class, class Animal(object): is the rule, 

print(isinstance(m, object))

#o = object()#creating an empty objects

print(issubclass(Mammal, Animal))#is Mammal a subclass of Animal
print(issubclass(Mammal, object))#is Mammal a subclass of object?
