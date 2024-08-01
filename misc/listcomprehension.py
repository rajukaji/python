#very useful technique in list comprehension found so far

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newList = ["odd" if i % 2 != 0 else "Even" for i in lst1]

print(newList)

# [ value if condition1 and condition or coditon else value for i in iterable]