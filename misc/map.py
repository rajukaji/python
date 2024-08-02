#easy way to understand map(function, iterable)

def passToMapToDoubleTheNumber(x):#arguement is must
    return x * 2

iterableList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#now lets call this function with map and put the changed value into a new list


newList = list(map(passToMapToDoubleTheNumber,  iterableList ) )

print(iterableList)
print(newList)

# it can be shortened using anonymous function called lambda, ok

lambdo = list( map( lambda x: x*3, iterableList ) )#to triple here
print(lambdo)
