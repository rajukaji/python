def is_long_pressed(name, typed):
    flag = True

    lst1 = {i: name.count(i) for i in name}
    lst2 = {i: typed.count(i) for i in typed}

    for i, j in lst1.items():
        if lst2[i] >= j:
            continue
        
        flag = False

    return flag


#check if name == 'hello'
#confirm if even if the long typed match the name, 
#eg, hheelllloo
print(is_long_pressed('kath', 'kaatthhh'))