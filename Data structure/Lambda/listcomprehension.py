items = {
    ("product1", 10), 
    ("product2", 9), 
    ("product3", 12), 
}

#lambda functions

#map
#lambda parameter:arguement
#map(function, iterable)
price = list(map(lambda item: item[1], items))
print(price)

#filter
#filter(function, iterable)
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

#writing comprehension
#for map
#[expression for parameter in iterables]
#preferred way to map in python is to use list comprehension
#instead map() and filter() function
#cleaner and more performant

#map
prices = [item[1] for item in items]
print(prices)

#filter
#[expression for expression in iterable if expression >= x]
filtered = [item for item in items if item[1] >= 10]
print(filtered)