def is_x_of_a_kind(deck, x):
    num = list(set(deck))
    dic = {}
    count = 0
    for i in range(len(deck)):
        if num[i] in deck:
            dic[num[i]] = count + 1
    flag = 0
    for i in dic:
        if dic[i] != x:
            flag = 1

    if flag == 0: 
        return True
    else:
        return False

listing = [1, 2, 2, 1, 4, 4, 5, 5]
print(is_x_of_a_kind(listing, 2)) #does the list has exact 2 copies for all the items