def insertion_sort(lst):
    # write your code here
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and key > lst[j]:
            lst[j+1] = lst[j]

            j = j - 1

        lst[j+1] = key
    
    return lst


# take integer inputs and convert it to a list
data_list = list(map(int, input('Enter elements of the list: ').split(' ')))

# call the insertion_sort() function
result = insertion_sort(data_list)

# print the sorted list
print(result)