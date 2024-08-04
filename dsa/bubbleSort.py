def bubble_sort(lst):
    swapped = False
    # outer loop to access each list element
    for i in range(len(lst)-1):#loops up to n-1, since last element doesn't require comparing
 
        # inner loop to compare list elements
        for j in range(len(lst) - 1-i):# -i to optimize the sort process
 
            # swap elements if necessary
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:#to break the loop if the list is already sorted
            break
 
    return lst       
 
data_list = [15, 16, 6, 8, 5]
print(f"Unsorted List: {data_list}")
 
sorted_list = bubble_sort(data_list)
 
print(f"Sorted List: {sorted_list}")

print(bubble_sort([1, 2, 3, 4, 5]))