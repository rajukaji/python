def divisors(n):
    return len([i for i in range(1, n+1) if n % i == 0])


print(divisors(15))
# 4 factors of 15, 
# i.e. 1, 3, 5, 15