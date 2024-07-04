class Point:
    def __init__ (self, x, y):#magic method
        self.x = x
        self.y = y


    def __str__(self):#magic method
        return f"({self.x}, {self.y})"
    
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point)
point.draw