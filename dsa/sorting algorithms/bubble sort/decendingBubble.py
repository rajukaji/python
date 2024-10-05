def bubble_sort(lst):
    # write your code here
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst



# take integer inputs and convert it to a list    
data_list = list(map(int, input("Input numbers with spacing:: ").split(' ')))


sorted_list = bubble_sort(data_list)
print(sorted_list)