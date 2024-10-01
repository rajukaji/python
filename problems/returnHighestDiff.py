def largest_gap(numbers):
    n = numbers
    return max([n[i+1] - n[i] for i in range(len(n)-1)])


lst = [1, 2, 3, 5, 8, 2, 9]

print(largest_gap(lst))

#return highest consecutive difference
#9 - 2 = 7 highest consequent in the list