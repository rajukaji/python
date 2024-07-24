# replace ___ with your code

# define a function to find the elements that can make target sum
def find_sum(numbers, target):

    # initialize the temporary list to avoid duplicates
    temp_list = []#to avoid duplicates

    # loop through the list
    for i in numbers:
        
        # if the difference of target and current element
        # is in the temporary list,
        # print the difference and the current element
        if (target - i) in temp_list: #avoiding repeated numbers
            print((target-i), i)

        # add the current element to the temporary list
        temp_list.append(i)


# call the function
numbers = [1, 5, 6, 3, 2, 4]
target_sum = 7
find_sum(numbers, target_sum)