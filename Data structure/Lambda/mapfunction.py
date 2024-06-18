items= [
    ("product1", 10),
    ("product2", 9),
    ("prodcut", 20), 
]#list of tuples of 2  item

#transform this list into different shape

prices = []

for item in items:
    prices.append(item[1])


print(prices)
#now we mapped or copied the 2nd item of the touple to the new empty list

#instead of this, we have map function too

x = map(lambda item: item[1], items)#takes 2 parameters map(function, *iterables)


#map function now iterate over items, ie, iterable
#and it will each item: item[1] on this iterable
for item in x: 
    print(item)

price = list(map(lambda item: item[1], items))
#converting map object into list object
#so we dont need a for loop now, simply print the list
print(price)