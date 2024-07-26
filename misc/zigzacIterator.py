def zigzag_iterator(list1, list2):
    lst = []
    
    for i in range(len(list1) + len(list2)):
        if i in range(len(list1)):
            lst.append(list1[i])
            
        if i in range(len(list2)):
            lst.append(list2[i])
            
    return lst

print(zigzag_iterator([1, 3, 5, 7], [2, 4, 6, 8])) 
#should print [1, 2, 3, 4, 5, 6, 7, 8]