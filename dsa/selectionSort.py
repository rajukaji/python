# Replace ___ with your code

def selection_sort(lst):
    # write your code here
    for i in range(len(lst)-1):
        minn = i
        for j in range(i+1, len(lst)):
            if lst[minn] < lst[j]:
                minn = j
        lst[minn], lst[i] = lst[i], lst[minn]
    return lst

# take integer input and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = selection_sort(data_list)
print(sorted_list)