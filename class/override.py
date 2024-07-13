class Base:
    def sayHello(self):
        print("hello")


class Derrived(Base):
    def sayHello(self):
        print("Buffalo")

        super().sayHello() #this calls the hello from the Base class now


objDerrived = Derrived()

objDerrived.sayHello()#calls the method of Derrived, since the method of Base class is overridden
