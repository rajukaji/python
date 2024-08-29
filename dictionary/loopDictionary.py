def find_it(seq):
    lst = {i: seq.count(i) for i in set(seq)}
    
    for i, j in lst.items():
        #with items()
        #i = key
        #j = value
        #  pairs

        if j % 2 != 0:
            return i
        #return key
        

print(find_it([1, 1, 1, 2, 2, 3, 3, 3, 3]))