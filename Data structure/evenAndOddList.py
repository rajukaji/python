def calculate_sum(numbers_list):
    even = sum([i for i in numbers_list if i % 2 == 0])
    odd = sum([i for i in numbers_list if i % 2 != 0])
    return [even, odd]
    # write your code here

# take list input
numbers_list = list(map(int,input('Enter list with space ::').split()))

# print sum of even and odd number
print(calculate_sum(numbers_list))

#return list of even sum and odd sum in a list