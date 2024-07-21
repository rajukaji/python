def find_highest_number(numbers_list):
    if len(numbers_list) == 1:
        return numbers_list[0]
    else:
        return max(numbers_list[0], find_highest_number(numbers_list[1:]))
    # write your code here

# take user input
numbers_list = list(map(int, input('enter numbers with space:: ').split())) # i.e. 1 2 3 12 10 33 100

# print the highest number
print(find_highest_number(numbers_list))