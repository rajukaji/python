#insertion sorting in dsa
# to keep 3 imaginary list in mindset
# 1. sorted part 2. unsorted part 3. key(generally, 1st element of unsorted part)
# single element list is already sorted
# let sorted list be only the 1st element[0] indexed, 
'''
def Insertion_Sort(lst):
    for i in range(1, len(lst)):#from 1 to length of the list
        key = lst[i]#FIRST ELEMENT of the unsorted list
        j = i - 1 #because we would need to access on the unsorted side

        while j >= 0 and key < lst[j]: # if the key of unsorted is less for ascending
            lst[j+1] = lst[j] #this is to shift the greater element in the sorted area to the unsorted in the place of key
            j = j - 1 #back to j is 0

        lst[j+1] = key

        return lst
        #this is inserting overridding jth with key

data =  [7, 4, 1, 3, 2]

print(f"Unsorted List: {data}")
sorted_list = Insertion_Sort(data)
print(f"Sorted List: {sorted_list}")'''

def insertion_sort(lst):
    
    for i in range(1, len(lst)):
        key = lst[i]
        
        j = i - 1
        
        while j >= 0 and lst[j] > key: # for descending check lst[j] < key
            lst[j + 1] = lst[j]
            j = j - 1

        lst[j + 1] = key
    
    return lst

data =  [7, 4, 1, 3, 2]

print(f"Unsorted List: {data}")
sorted_list = insertion_sort(data)
print(f"Sorted List: {sorted_list}")