# function to perform binary search
def binary_search(lst, target):
    
    # set low and high index
    low = 0
    high = len(lst) - 1
    
    # if low is greater than high,
    # the element is not found in the list 
    while low <= high:
        
        # find middle element
        mid = (low + high) // 2
        
        # if target value is equal to middle element
        # return the element
        if target == lst[mid]:
            return mid
        
        # if target value is less than the middle element
        # update high to mid - 1 
        elif target < lst[mid]:
            high = mid - 1
        
        # if target value is less than the middle element
        # update low to mid + 1 
        else:
            low = mid + 1
    
    return None
 
lst = [4, 5, 6, 7, 8, 9, 10]
# sorted list
 
# set a target value
target_value = 7
 
result = binary_search(lst, target_value)
 
if result:
    print(f"Element {target_value} is found at index {result}")
else:
    print(f"{target_value} is not found in the list")