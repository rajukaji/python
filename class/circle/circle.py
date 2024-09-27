# class name(object):

class Circle(object):
    # always pass object, this is the parent of the class
    # the parameters are passed,
    # self.parameters are the real attributes

    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    def Area(self):
        # circle method
        return self.radius ** 2 * 3.14159
    
    
circleObject = Circle('red', 12)
print(circleObject.color)
print(circleObject.Area())