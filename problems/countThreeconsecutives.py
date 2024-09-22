def check_consecutive_numbers(numbers):
    coun = [i for i in numbers if numbers.count(i) == 3]
    return len(coun) == 3

print(check_consecutive_numbers([1, 3, 2, 2, 2]))