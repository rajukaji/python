def is_ugly(num):
    factor = 0

    while 1 == 1:
        if num % 2 == 0:
            num /= 2
            continue
        
        elif num % 3 == 0:
            num /= 3
            continue

        elif num % 5 == 0:
            num /= 5
            continue

        return True if num == 1 else False

        

# if the number is divisible by either 2, 3, and 5 we keep on dividing, until the time it cannot be divided further
# if the remainder is 1 its an ugly number, else, its not
print(is_ugly(6))