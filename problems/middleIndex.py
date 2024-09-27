def gimme(input_array):
    # Implement this function
    mid = 0
    s = input_array
    for i in input_array:
        if not i == min(s) and not i == max(s):
            mid = i
    
    return s.index(mid)
    # return inputArray.index(sorted(inputArray)[1])
    # one line code from codewars


# find index position of the middle value among 3

print(gimme([5, 7, 1]))
# 0 because, between 1 and 7 there lies 5, and its index position is 0