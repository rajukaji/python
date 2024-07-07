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