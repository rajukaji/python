def echoOdd(lst):
    a, b = set(lst)
    return a if lst.count(a) == 1 else b


lst = [1, 1, 1, 1, 3, 1, 1, 1, 1]

print(echoOdd(lst))#return odd one, its 3, as its occurance is only one time, 