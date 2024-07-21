def find_index(lst, n):
    count = 0
    for i in lst:
        
        if n == i:
            break
        
        count += 1

    return count

print(find_index([1, 2, 3, 4, 5], 4))