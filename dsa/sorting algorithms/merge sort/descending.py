def merge_sort(lst):
    if len(lst) <= 1:
        return lst


    mid = len(lst) // 2

    left_part = merge_sort(lst[:mid])
    right_part = merge_sort(lst[mid:])

    return merge(left_part, right_part)


# define the merge() function
def merge(left,right):    
    i = 0
    j = 0
    result = []


    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    # adding remaining
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# take integer inputs and convert it to a list
data_list = list(map(int, input('Enter list :: ').split(' ')))

sorted_list = merge_sort(data_list)

print(sorted_list)