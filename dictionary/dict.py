def group_items(lst):
    l = {}

    index = []

    for i in range(len(lst)):
        if lst[i] in l:
            l[lst[i]] += [i]
        else:
            l[lst[i]] = [i]
        
    return l

#generate the dictionary with values equal to a list of the value indexes

print(group_items(['apple', 'banana', 'mango', 'apple', 'mango']))