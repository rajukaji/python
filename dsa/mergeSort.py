def merge(left, right):
    output = [ ]
 
    i = 0
    j = 0
 
    while i < len(left) and j < len(right): 
 
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j]) 
            j += 1
 
    # copy the remaining elements to output
    output.extend(left[i:])
    output.extend(right[j:])
 
    return output
 
 
print(merge([5], [8]))    # [5, 8]
print(merge([8], [5]))    # [5, 8]
print(merge([3, 4], [7, 10]))  # [3, 4, 7, 10]
print(merge([3, 4], [7, 10, 11]))  # [3, 4, 7, 10, 11]
