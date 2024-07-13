# Replace ___ with your code

class Coordinate:
    def __init__(self, x, y):
        self.x_cor = x
        self.y_cor = y


    def add_coordinates(self, passObject):

        add_x = self.x_cor + passObject.x_cor#add x coordinates
        add_y = self.y_cor + passObject.y_cor#add y coordinates

        returnObject = Coordinate(add_x, add_y) #return object with teh required args values
        return returnObject


c1 = Coordinate(5, 6)
c2 = Coordinate(7, 9)

c3 = c1.add_coordinates(c2)#create a 3rd object, call the method of c1 by passing c2 object as arguement

print(c3.x_cor)
print(c3.y_cor)


#can do the same with adding imaginary numbers


        