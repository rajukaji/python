"""
def functionName(parameters):
    pass
"""
#def = function definition

def increment(number, by):
    return (number, number + by)
    #return multiple values, number is original number
#twoline breaks after a function, from pep8
#twoline breaks after a function, from pep8

print(increment(2, 3))
#gives tuple, cannot modify the list
listing = (1, 2, 3)# is a tuple, cannot modify the list


#keyword arguements to make codes more readable
print(increment(2, by=3))#increment 2 by 3

#type anotation

def func(number: int, by: int=1) -> tuple:
    return (number, number + by)

print(func(2))
