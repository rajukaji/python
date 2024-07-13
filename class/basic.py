#basic creation of class and object

class Class:
    pass
#we can use pass, since the object cannot be empty

object1 = Class()
object2 = Class()

#lets include everything now

class Person:
    #adding method/or function
    def isHappy(self):
        return True
'''
We must always use self as the first argument in the function definition. 
This self takes the value of the object calling it.
'''    


petu = Person()
print(petu.isHappy())
#prints True, accessing the method of the class Person()

