def multiply(a, b):
    return a * b

print(multiply(2, 3))

#pass arbitary numbers

def mult(*listing):# * before a number is a tuple
    print(listing)
    total = 1
    for number in listing:
        total *= number
    return total
    
print(mult(2, 3, 4, 5))#multiply all 