def insert_element(lst,index,value):
    lst.insert(index, value)
    return lst

print(insert_element([1, 2, 3, 5], 3, 4))
#insert into a list, with index and value, insert(index, value)



lst = ['a', 'b', 'd', 'e']
print(lst)

lst.insert(2, 'c')
# insert into  the second item

print(lst)