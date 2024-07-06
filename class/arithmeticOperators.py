class Arithmetic:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Arithmetic(self.x + other.x, self.y + other.y)

#add two points together
a = Arithmetic(3, 2)
b = Arithmetic(2, 5)
add = a + b
print(add.x)#add 3 and 2
print(add.y)#add 2 and 5