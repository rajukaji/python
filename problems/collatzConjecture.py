def collatz_conjecture(n):
    lst = [n]

    while True:
        if n == 1:
            # lst.append(1)
            # lst.append(1)
            break

        if n % 2 == 0:
            # lst.append(n)
            n = n // 2
            lst.append(n)
            continue
        
        if n % 2 != 0:
            n = n*3+1
            lst.append(n)

        
    return lst

# if the number is even divide by 2 and write quotient
# if the number is odd multiply by 3 and add 1 to the number
# stop the series if the number is equal to 1

print(collatz_conjecture(6))