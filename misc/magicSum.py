def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

#find that index of the list that either side of the list sums are equal
#list [1, 2, 3, 4, 3, 2, 1]
# the index 3 is the value 4, before 4,  1+2+3 is 6 and also after 4 3+2+1 is 6, 

print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
