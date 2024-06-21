items= [
    ("product1", 10),
    ("product2", 9),
    ("prodcut3", 20), 
]#list of tuples of 2  item

#filter(function, *iterables)

filteredprice = list(filter(lambda item: item[1]  >= 10 , items))
#iterms price greater or equal to 10
print(filteredprice)