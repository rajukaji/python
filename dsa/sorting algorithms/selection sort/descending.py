def selection_sort(lst):
   
    for  i in range(len(lst) - 1):
        small = i

        for j in range(i + 1, len(lst)):
            if lst[small] < lst[j]:
                small = j
        
        lst[small], lst[i] = lst[i], lst[small]
    return lst


data_list = list(map(int, input('Enter list elements:').split(' ')))

sorted_list = selection_sort(data_list)
print(sorted_list)