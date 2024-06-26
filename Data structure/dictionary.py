#very powerful data structure
#key value pair
#{'a' : 1 ,  'e' : 2}
#immutable types for keys
#value can be of any type, there is no limitations, 
#dict() function
#other functions, 
#list(), tuple(), set()

point = {"x": 1, "y": 2}

#we use function too
point = dict(x=1, y=2)
#we must pass one or more keyword arguements

print(point["x"])
#index is name of key
#we cannot use numeric index, though

point["x"] =10
print(point["x"])

point["z"] = 20
print(point)

#we can access values in different ways
if "a" in point:
    print("Exists")

#we can also use get() method
print(point.get("y", 0))
#0 is default value to return if y doesn't exist
#replace 0 with any other values


print(point)

for key in point:
    print(key, point[key])

#another way to iterate over dictionary
for x in point.items():#we get the tuple now
    print(x)

#for the same as above tuple
#use
for key, value in point.items():
#unpacking to key and value above
    print(key,value)