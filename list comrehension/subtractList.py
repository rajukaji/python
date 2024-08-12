def subList(a, b):
    return [i for i in a if i not in b]
#only return the elements from a if its not in b, the similar elements are ommited


a = [1, 5, 4, 3, 6, 6, 7]
b = [1, 3, 7, 6]
print(subList(a, b))