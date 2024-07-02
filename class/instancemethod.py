class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    @classmethod #this is a decorator to define classmethod in python
    def zero(cls):#class method uses cls parameter
        return cls(0, 0) #initial values

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()#this is a instance method

#we use class method when we dont need the instance methods

point = Point.zero()
#method defined at the class level
point.draw()