# Scenario: Car dealership's inventory management system
# You are working on a Python program to simulate a car dealership's inventory management system. The system aims to model cars and their attributes accurately.

# ### Task-1. You are tasked with creating a Python program to represent vehicles using a class. Each car should have attributes for maximum speed and mileage. 

class Vehicle(object):
    #constructor 
    color = 'white'
    # DEFAULT COLOR
    
    def __init__(self, speed, mileage):
        self.speed = speed
        self.mileage = mileage


    def seatCapacity(self, capacity):
        self.capacity = capacity
    

    def display_info(self):
        print(f"Color : {self.color}")
        print(f"Max_speed : {self.speed}")
        print(f"Mileage: {self.mileage}")



Obj1 = Vehicle(200, 50000)
Obj1.seatCapacity(5)
Obj1.display_info()

Car = Vehicle(180, 75000)
Car.seatCapacity(4)
Car.display_info()