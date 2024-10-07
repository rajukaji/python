def quick_sort(lst):
    # write you code here    
    length = len(lst)

    if length <= 1:
        return lst
    else:
        mid_index = length//2
        pivot = lst.pop(mid_index)
        # middle element as the pivot
        # iterable.pop(index)
    
    left_list = []
    # list greater than pivot

    right_list = []
    # list lesser than pivot

    for i in lst:
        if i > pivot:
            left_list.append(i)
        else:
            right_list.append(i)
    

    return quick_sort(left_list) + [pivot] + quick_sort(right_list)

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = quick_sort(data_list)

print(sorted_list)