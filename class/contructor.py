#constructor

class Point:
    default_color = "red" #class attributes are shared to all the instances of class
    #they are shared all instances of class, if they are changed they are visible in all instances of class
    #they are like global

    def __init__(self, x, y): #magic method
        self.x = x
        self.y = y
#self is a reference to the current point object


    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
print(point.x)

point.draw()

#we can define the attributes of the objects later on too
point.z = 10 

another = Point(3, 4)
another.draw()
#x, y, and z are only instance level attribute now


