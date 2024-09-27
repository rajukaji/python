class Car(object):
    def __init__(self,make,model,color):

        self.make=make
        self.model=model
        self.color=color
        self.owner_number=0 


    def car_info(self):

        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)


    def sell(self):

        self.owner_number=self.owner_number+1


make="BMW"
model="M3"
color="red"

My_car = Car(make, model, color)

My_car.car_info()

for i in range(5):
    My_car.sell()
    
    
My_car.car_info()