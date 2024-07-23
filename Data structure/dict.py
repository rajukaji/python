def group_items(lst):
    dic = {'apple': [1, 2, 3]}
    #print(type(dic))
    dup = list(set(lst))
   # print(dup)
    ##print(len(lst))
    #print(dup[0])
    index = []
    for i in range(0, len(lst)):
        if lst[i] in dup:
            dic[lst[i]] = index.append(i)
        
    return dic

listing = ['apple', 'banana', 'apple', 'banana', 'apple']

print(group_items(listing))
