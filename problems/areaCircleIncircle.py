import math
def calculate_circle_areas(square_area):
    r = math.sqrt(square_area )/2
    return (round( r**2 * 3.14159, 2),  round( 3.14159 * (math.sqrt(square_area/2)**2), 2))

print(calculate_circle_areas(16))
# return a tuple containing the areas of incircle adn circum circle rounded
# off to two decimal places. 

# The formula for calculating area is pie * r ** 2, where r is radius

# The radius for incircle is half of side length, while for circumcircle
# its half of diagonal length