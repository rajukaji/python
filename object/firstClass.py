class FirstClass:
    def sayHello(self): #self is compulsory, it reference to the instance or object when it is called
        print("Hello!")

#create object by assigning the class to an object

firstObject = FirstClass() #passing nothing

print(firstObject.sayHello()) #call method
#also returns none as the method is not returning anything
#so you need not print. just call the method

firstObject.sayHello()