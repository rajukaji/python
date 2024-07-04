#comparing two objects
class Compare:
    def __init__ (self, x, y):
        self.x = x
        self.y = y


    def __eq__ (self, other):
        return self.x == other.x and self.y == other.y



point1 = Compare(1, 2)
point2 = Compare(2, 3)
print(point1 == point2)#this will only compare the address of point 1 and point 2 unless use the magic methods

