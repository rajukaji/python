# function to perform  linear search
def linear_search(lst, target):
    
    # traverse through each element
    for index, element in enumerate(lst):
        
        # compare each element with a target value
        if element == target:
            return index
    
    # return None if the target isn't found in lst
    return None
 
lst = [9, 10, 5, 8, 7, 4, 11, 6, 15, 3]
 
# set a target value
target_value = 4
 
result = linear_search(lst, target_value)
 
if result:
    print(f"Index of the target value: {result}")
else:
    print("Target value not found in the list.")
