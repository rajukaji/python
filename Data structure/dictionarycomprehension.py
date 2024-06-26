values = []#empty list

for x in range(5):
    values.append(x * 2)#iterating over this object
    #multiplied by 2 and added to the list of values

print(values)

#we can either use map function or use 
#now use list comprehension

#[expression for item in items]
#items iterable, expression is to do something to item

values = [x * 2 for x in range(5)]#same as above 
print(values)

#we can use this with sets and dictionaries too. 

values = {x * 2 for x in range(5)}#with curly braces
print(values)


#dictionary {1 : "a", 2: "b"}
values = {}

for x in range(5):
    values[x] = x * 2

print(values)#instead of doing this, 


values = {x: x * 2 for x in range(5)}#keyvalue pair of dictionary comprehension
print(values)

#now for tuples
values = (x * 2 for x in range(5))#actually generator object
print(values)
