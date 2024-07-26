import math
def calculate_primorial(n):
    lst = [i for i in range(2, n+1)]
    flag = 0
    prime = []
    for i in lst:
        for j in range(2, n+1):
            if i % j == 0:
                flag += 1 # increase flag every time, as we only want it to increase only one time to be it a prime number
                #since, it should only be divisible by only itself, no other factors are accepted for a prime number
        if flag == 1:
            prime.append(i)#append to the prime lists
        flag = 0#resetting the flag, the the next number in the sequence of lst

    return math.prod(prime)

#products of all the prime numbers up to the n numbers is primorial number, 

print(calculate_primorial(5)) # prints 30 as the products of the primes, 2, 3, and 5 is 30