# Replace ___ with your code

def counting_sort(lst):
    # write your code here
    if len(lst) <= 1:
        return lst
    

    max_item = max(lst)

    counting_list = [0] * (max_item + 1)

    for num in lst:
        counting_list[num] += 1
    
    result = []

    for index, value in enumerate(counting_list):
        result.extend([index] * value)

    return result[::-1]


# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = counting_sort(data_list)

print(sorted_list)